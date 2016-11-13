from django.conf.urls import url
from rest_framework import routers

from yle.views import NewsViewSet, LastNewsView

router = routers.DefaultRouter(trailing_slash=True)


router.register(r'^news', NewsViewSet,
                base_name='news')

urlpatterns = [
   url(r'^news/latest/', LastNewsView.as_view()),
]

urlpatterns += router.urls
