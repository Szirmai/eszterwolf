from django import forms
from main import models

class PaintingCategoryForm(forms.ModelForm):
    class Meta:
        model = models.PaintingCategory
        fields = ('name', )
        
class MappingCategoryForm(forms.ModelForm):
    class Meta:
        model = models.MappingCategory
        fields = ('name', )
        
class ConnectingCategoryForm(forms.ModelForm):
    class Meta:
        model = models.ConnectingCategory
        fields = ('name', )
        
class PaintingForm(forms.ModelForm):
    class Meta:
        model = models.Painting
        fields = '__all__'
        
class MappingForm(forms.ModelForm):
    class Meta:
        model = models.Mapping
        fields = '__all__'
        
class ConnectingForm(forms.ModelForm):
    class Meta:
        model = models.Connecting
        fields = '__all__'