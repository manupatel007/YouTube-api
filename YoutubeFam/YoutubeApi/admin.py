from django.contrib import admin
from YoutubeApi import models
# Register your models here.
class YTAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.YoutubeData,YTAdmin)