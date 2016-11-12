from django.test import TestCase

from yle.models import News
from yle.tasks import fetch_news, fetch_audio_url


class YleTests(TestCase):

    def test_it(self):
        fetch_news()
        # Default list is 12
        self.assertEqual(News.objects.all().count(), 12)

    def test_one(self):
        fetch_news()
        n = News.objects.all().last()
        fetch_audio_url(n)
        n.refresh_from_db()
        # There's at least some url with an mp3 file.
        self.assertRegex(n.audio_url, r'http.?:\/\/.*\.mp3')

    def test_serializer(self):
        n = News.objects.create(external_id='123',
                                audio_url='http://url.mp3',
                                title='The title',
                                created='2014-01-01T14:00:00Z')
        res = self.client.get('/news/')
        self.assertEqual(res.status_code, 200)

        data = res.json()
        print(data)
        self.assertEqual(len(data), 1)
        news = data[0]
        self.assertEqual(str(n.uuid), news['uid'])


