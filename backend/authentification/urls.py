from django.conf.urls import url
from . import api

urlpatterns = [
	url(r'^user$', api.ObtainAuthUser.as_view() ),
	url(r'^pro/login$', api.ObtainAuthToken.as_view() ),
	url(r'^verification-email$', api.VerificationEmail.as_view() ),
]