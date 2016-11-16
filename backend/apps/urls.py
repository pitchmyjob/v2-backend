from django.conf.urls import include, url
from rest_framework.routers import SimpleRouter, DefaultRouter

from backend.apps.pro.urls import pro_urls
from backend.apps.datas.urls import datas_urls

router = DefaultRouter()
#router.register(r'pro', ProViewSet, base_name='pro')

router_urls = router.urls

urlpatterns = [
    url(r'^', include(router_urls)),
    url(r'^pro/', include(pro_urls)),
    url(r'^datas/', include(datas_urls)),
]
