from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.QR_genration)
admin.site.register(models.url_shortener)
admin.site.register(models.link_detection)
admin.site.register(models.Contact)

#Twillo API Key - CQ78KU8PRUL15VY6CA6B2APY