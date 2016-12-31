from django.conf.urls import url
from . import api

job_urls = [
    url(r'^(?P<job>[0-9]+)/questions$', api.ListCreateJobQuestion.as_view(), name="job_questions"),
    url(r'^(?P<job>[0-9]+)/question/(?P<pk>[0-9]+)$', api.RetrieveJobQuestion.as_view(), name="job_questions"),
]