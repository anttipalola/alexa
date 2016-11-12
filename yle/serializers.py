from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, CharField, UUIDField

from alexa.settings import RADIO_LINK_BASE
from yle.models import News


class NewsSerializer(ModelSerializer):

    uid = UUIDField(source='uuid')
    updateDate = CharField(source='created')
    titleText = CharField(source='title')
    streamUrl = CharField(source='audio_url')
    mainText = CharField(source='content')
    redirectionUrl = SerializerMethodField('get_redirection')

    def get_redirection(self, obj):
        return RADIO_LINK_BASE + obj.external_id

    class Meta:
        model = News
        fields = ['uid', 'updateDate',
                  'titleText', 'streamUrl',
                  'mainText', 'redirectionUrl']
