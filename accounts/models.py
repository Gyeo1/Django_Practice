from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    address=models.CharField(max_length=100, blank=True)
    zipcode=models.CharField(max_length=7, blank=True )#집 주소
post_save