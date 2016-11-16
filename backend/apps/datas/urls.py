from django.conf.urls import url
from . import api

datas_urls = [
    url(r'^industry', api.IndustryList.as_view() ),
    url(r'^employes', api.EmployesList.as_view() ),
]