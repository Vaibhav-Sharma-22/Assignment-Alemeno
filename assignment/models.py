from django.db import models

# Create your models here.
class Kid(models.Model):
    Kid_Name = models.CharField('Name', max_length=100)
    Kid_Age = models.IntegerField('Age')
    Parent_Phone_Number = models.IntegerField(blank=True)
    Parent_Email_Address = models.EmailField('Email Address')

class Image(models.Model):
    Kid = models.ForeignKey(Kid, blank=True, null=True)
    Image_URL = models.URLField()
    Created_On = models.DateTimeField()
    Updated_on = models.DateTimeField()
    Is_Approved = models.BooleanField()
    Approved_by = models.CharField("", max_length=50)
    FoodGroup = models.Choices
