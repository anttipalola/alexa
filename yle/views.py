from rest_framework import mixins, viewsets

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from yle.models import News
from yle.serializers import NewsSerializer


class NewsViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    View for listing news.
    """

    permission_classes = (AllowAny,)
    serializer_class = NewsSerializer
    # Latest first
    queryset = News.objects.all().order_by('-created')


class LastNewsView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):
        n = News.objects.all().order_by('created').last()
        data = NewsSerializer(instance=n)
        return Response(data.data)
