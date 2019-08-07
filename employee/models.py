from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token

class emp(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	empid=models.CharField(max_length=5,blank=True)
	housename=models.CharField(max_length=50,blank=True)
	city=models.CharField(max_length=30,blank=True)
	state=models.CharField(max_length=30,blank=True)
	pincode=models.IntegerField(blank=True,null=True)
	mobile=models.BigIntegerField(blank=True,null=True)
	boss=models.IntegerField(blank=True,null=True)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = emp.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)	
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)