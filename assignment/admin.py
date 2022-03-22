from django.contrib import admin
from .models import Kid, Image
# Register your models here.
admin.site.register([Kid, Image])
