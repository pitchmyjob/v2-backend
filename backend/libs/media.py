import base64
import os
import uuid
from django.core.files.base import ContentFile
from rest_framework import serializers


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        basestring = (str, bytes)
        if isinstance(data, basestring) and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension

            data = ContentFile(base64.b64decode(imgstr), name="image." + ext)

        return super(Base64ImageField, self).to_internal_value(data)



def generate_filename_pro(self, filename):
    filename, file_extension = os.path.splitext(filename)
    name = str(uuid.uuid4()) + str(file_extension)
    url = "pro/%s/%s" % ( self.id, name)
    return url

def generate_filename_user(self, filename):
    filename, file_extension = os.path.splitext(filename)
    name = str(uuid.uuid4()) + str(file_extension)
    url = "user/%s/%s" % ( self.id, name)
    return url

def generate_filename_job(self, filename):
    filename, file_extension = os.path.splitext(filename)
    name = str(uuid.uuid4()) + str(file_extension)
    url = "job/%s/%s" % ( self.id, name)
    return url