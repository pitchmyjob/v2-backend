from django.conf.urls import url
from . import api

pro_urls = [
	url(r'^signup$', api.SignUpPro.as_view(), name="pro_signup" ),
	url(r'^$', api.retreiveUpdatePro.as_view(), name="pro_pro" ),
]