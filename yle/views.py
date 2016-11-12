from rest_framework import mixins, viewsets

from rest_framework.permissions import AllowAny

from yle.models import News
from yle.serializers import NewsSerializer


class NewsViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    View for listing news.
    """

    permission_classes = (AllowAny,)
    serializer_class = NewsSerializer
    queryset = News.objects.all()
