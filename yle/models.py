import uuid as uuid
from django.db import models


class News(models.Model):
    """
    News item contains the necessary information to read out the news.
    """
    # External ID, might be textual or number.
    external_id = models.CharField(max_length=128)

    uuid = models.UUIDField(default=uuid.uuid4)

    # Main title for the news
    title = models.CharField(max_length=256, default="")

    # Body/content of the news
    content = models.TextField(default="")

    # Url to an audio file that contains the news
    audio_url = models.URLField(default="", blank=True)

    # Timestamps
    created = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} ({})".format(self.external_id, self.created)
