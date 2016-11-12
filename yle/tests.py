from django.test import TestCase

# Create your tests here.
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
