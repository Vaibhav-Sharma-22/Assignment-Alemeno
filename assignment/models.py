from distutils.command.upload import upload

from random import choice
from sre_constants import SUCCESS
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings


FOOD_CHOICES = (
    ("1", "Veg"),
    ("2", "Fruit"),
    ("3", "Grain"),
    ("4", "Protein"),
    ("5", "Dairy"),
    ("6", "Confectionary"),
    ("7", "Unknown")
)
# Create your models here.


#Kid model
class Kid(models.Model):
    Kid_Name = models.CharField('Name', max_length=100)
    Kid_Age = models.IntegerField('Age')
    Parent_Phone_Number = models.IntegerField(blank=True)
    Parent_Email_Address = models.EmailField('Email Address')

    def __str__(self):
        return self.Kid_Name
    

#Table model 
class Image(models.Model):
    Kid = models.ForeignKey(Kid, blank=True, null=True, on_delete=models.CASCADE)
    Image_URL = models.URLField()
    Group = models.CharField(choices=FOOD_CHOICES, max_length=20, default='7')
    Created_On = models.DateTimeField(auto_now_add=True)
    Updated_on = models.DateTimeField()
    Is_Approved = models.BooleanField()
    Updated_by = Kid.__getattribute__


#Logic for Unknown food item mail send
def image_post_save(*args, **kwargs):
    instance = kwargs['instance']
    if instance.Group=='7':
        
        send_mail('Unknow Food Item', 'Unknown Food Item in the Image', settings.EMAIL_HOST_USER, [instance.Kid.Parent_Email_Address])
        pass
    pass

post_save.connect(image_post_save, sender=Image)
