from rest_framework.serializers import ModelSerializer, CharField, UUIDField

from yle.models import News


class NewsSerializer(ModelSerializer):

    guid = UUIDField(source='uuid')
    updateDate = CharField(source='modified')
    titleText = CharField(source='title')
    streamUrl = CharField(source='audio_url')
    mainText = CharField(source='content')

    class Meta:
        model = News
        fields = ['guid', 'updateDate',
                  'titleText', 'streamUrl',
                  'mainText']
