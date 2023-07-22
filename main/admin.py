from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.MappingCategory)
admin.site.register(models.Mapping)
admin.site.register(models.ConnectingCategory)
admin.site.register(models.Connecting)
admin.site.register(models.PaintingCategory)
admin.site.register(models.Painting)