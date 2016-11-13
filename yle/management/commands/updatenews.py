from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Updates news items and their urls'

    def handle(self, *args, **options):
        from yle.tasks import fetch_news, fetch_audio_urls
        fetch_news()
        fetch_audio_urls()
        return ' == News updated =='
