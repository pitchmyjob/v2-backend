from django.db import models
from backend.apps.pro.models import Pro
from backend.authentification.models import User
from easy_thumbnails.fields import ThumbnailerImageField
from backend.libs.media import generate_filename_job
from backend.apps.datas.models import Contract, ContractTime
from django.contrib.postgres.fields import ArrayField

class Job(models.Model):
    pro             = models.ForeignKey(Pro)
    company         = models.CharField(max_length=250, null=True)
    title           = models.CharField(max_length=250, null=True)
    description     = models.TextField(null=True)
    mission         = models.TextField(null=True, blank=True)
    profile         = models.TextField(null=True, blank=True)
    image           = ThumbnailerImageField(upload_to=generate_filename_job, blank=True)
    contracts       = models.ManyToManyField(Contract, blank=True)
    contract_time   = models.ManyToManyField(ContractTime, blank=True)
    tags            = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    video_url       = models.CharField(max_length=250, null=True, blank=True)
    view            = models.IntegerField(default=0)

    latitude        = models.FloatField(null=True, blank=True)
    longitude       = models.FloatField(null=True, blank=True)
    street_number   = models.CharField(max_length=250, null=True, blank=True)
    route           = models.CharField(max_length=250, null=True, blank=True)
    locality        = models.CharField(max_length=250, null=True, blank=True)
    administrative_area_level_2 = models.CharField(max_length=250, null=True, blank=True)
    administrative_area_level_1 = models.CharField(max_length=250, null=True, blank=True)
    country         = models.CharField(max_length=250, null=True, blank=True)

    date_created    = models.DateField(auto_now_add=True, null=True)
    last_update     = models.DateTimeField(auto_now=True, null=True)
    date_posted     = models.DateTimeField(null=True, blank=True)

    complete        = models.BooleanField(default=False)
    active          = models.BooleanField(default=False)
    paid            = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.pk:
            pass
        super(Job, self).save(*args, **kwargs)


class JobQuestion(models.Model):
    question = models.CharField(max_length=250, null=True)
    nb 		 = models.IntegerField(null=True)
    job 	 = models.ForeignKey(Job, related_name='questions', null=True, blank=True)

    def __str__(self):
        return str(self.question)

    class Meta :
        ordering = ['nb']