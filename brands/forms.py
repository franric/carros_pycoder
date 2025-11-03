from django import forms
from brands.models import Brand

class BrandModelForm(forms.ModelForm):
  class Meta:
    model = Brand
    fields = '__all__'
