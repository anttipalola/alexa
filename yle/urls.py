from rest_framework import routers

from yle.views import NewsViewSet

router = routers.DefaultRouter(trailing_slash=True)


router.register(r'^news', NewsViewSet,
                base_name='news')
