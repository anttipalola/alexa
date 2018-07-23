from urllib import request

from IPython.utils.tz import utcnow
from bs4 import BeautifulSoup

from alexa.settings import RADIO_LINK, RADIO_LINK_BASE
from yle.models import News


def fetch_news():
    """
    Fetch current news items from yle website.
    """
    page = request.urlopen(RADIO_LINK)

    # Need to use html5lib though it's slow, lxml parser didn't work properly
    soup = BeautifulSoup(page, "html5lib")
    items = soup.select('ul.program-list li')
    for el in items:
        identity = el.get('data-id')

        start = el.select('[itemprop="publication"] time')[0]\
            .get('datetime')
        name = el.select('[itemprop="name"]')[0].next_element

        print("item with date", start)
        News.objects.get_or_create(external_id=identity,
                                   defaults={'created': start,
                                             'title': name
                                             })

    print("created {} items".format(len(items)))


def fetch_audio_urls():
    """
    Try to get audio urls for all the items
    """
    # Only for today's news
    news = News.objects.filter(audio_url="",
                               created__gte=utcnow().replace(hour=0))
    for n in news:
        fetch_audio_url(n)
    print("tried fetching urls for {} items".format(news.count()))

    news_to_delete = News.objects.filter(audio_url="")
    print("Delete {} news without audio".format(news_to_delete.count()))
    news_to_delete.delete()


def fetch_audio_url(news: News):
    """
    Get audio url for a single news item.

    :param news: News to fetch url for.
    """
    page = request.urlopen(RADIO_LINK_BASE + news.external_id)
    soup = BeautifulSoup(page, "lxml")
    s = soup.select('div[itemprop="audio"] [itemprop="contentUrl"]')

    if len(s) > 0:
        url = s[0].get('href')
        news.audio_url = url
        news.save(update_fields=['audio_url'])
