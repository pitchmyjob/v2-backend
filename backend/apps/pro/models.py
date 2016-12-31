from __future__ import unicode_literals, absolute_import
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from backend.authentification.models import User
from backend.apps.datas.models import Industry, Employes
from easy_thumbnails.fields import ThumbnailerImageField
from backend.libs.media import generate_filename_pro
from backend.libs.email import AsyncEmail


class Pro(models.Model):
	company			= models.CharField(_('Raison sociale'), max_length=250, null=True)
	web_site		= models.CharField(_('Site web'), max_length=250, null=True, blank = True)
	description		= models.TextField(_('Description'), null=True, blank = True)
	phone			= models.CharField(_('Phone'), null=True, blank = True, max_length=250)
	industry 		= models.ForeignKey(Industry,  default=1)
	employes 		= models.ForeignKey(Employes, null=True)
	ca 				= models.CharField(max_length=250, null=True, blank=True)
	video_url 		= models.CharField(max_length=250, null=True, blank=True)
	address 		= models.CharField(max_length=250, null=True, blank=True)
	latitude 		= models.FloatField(null=True, blank=True)
	longitude 		= models.FloatField(null=True, blank=True)
	street_number 	= models.CharField(max_length=250, null=True, blank=True)
	route 			= models.CharField(max_length=250, null=True, blank=True)
	cp 				= models.CharField(max_length=250, null=True, blank=True)
	locality 		= models.CharField(max_length=250, null=True, blank=True)
	administrative_area_level_2 = models.CharField(max_length=250, null=True, blank=True)
	administrative_area_level_1 = models.CharField(max_length=250, null=True, blank=True)
	country		 	= models.CharField(max_length=250, null=True, blank=True)
	image 			= ThumbnailerImageField(upload_to=generate_filename_pro, null=True)

	def signup(**kwargs):
		user = User.objects.create_user(kwargs['email'], kwargs['email'], kwargs['password'], kwargs['first_name'], kwargs['last_name'])
		pro = Pro.objects.create(company=kwargs['company'], phone=kwargs['phone'])
		user.pro = pro
		user.save()
		user.add_group(['pro', 'pro_admin'])
		mail = AsyncEmail(to=[user.email], subject="Bienvenue sur Pitch my Job", template="member/inscription.html", context={ "name" : user.first_name })
		mail.send()
		return pro

	def save(self, *args, **kwargs):
		if not self.pk:
			pass
		super(Pro, self).save(*args, **kwargs)
