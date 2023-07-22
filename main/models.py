from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class MappingCategory(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']
    
class Mapping(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='mapping/', null=True)
    category = models.ForeignKey(MappingCategory, on_delete=models.CASCADE)
    page = RichTextUploadingField(max_length=1000000)
    
    
class ConnectingCategory(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']
        
class Connecting(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='mapping/', null=True)
    category = models.ForeignKey(ConnectingCategory, on_delete=models.CASCADE)
    page = RichTextUploadingField(max_length=1000000)

class PaintingCategory(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']
        
class Painting(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(PaintingCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="paintings/")
    size1 = models.PositiveIntegerField()
    size2 = models.PositiveIntegerField()
    date = models.CharField(max_length=200)
    crated = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']
    
    
    