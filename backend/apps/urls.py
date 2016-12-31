from django.conf.urls import include, url
from rest_framework.routers import SimpleRouter, DefaultRouter

from backend.apps.pro.urls import pro_urls
from backend.apps.datas.urls import datas_urls
from backend.apps.job.urls import job_urls

from backend.apps.job.api import JobViewSet

router = DefaultRouter()
router.register(r'job', JobViewSet, base_name='job')

router_urls = router.urls

urlpatterns = [
    url(r'^', include(router_urls)), 
    url(r'^pro/', include(pro_urls)),
    url(r'^datas/', include(datas_urls)),
    url(r'^job/', include(job_urls)),
]
