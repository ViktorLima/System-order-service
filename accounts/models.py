from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import *
from service.models import Cliente
from django import forms




# Create your models here.
# Register your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    registration = models.CharField(max_length=25)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
     Profile.objects.create(user_name=instance, )
     post_save.connect(create_user_profile, sender=User)

class FormCustomer(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ()
