#...
from .models import Keys
from django import forms
# from django.template.defaultfilters import slugify

#class KeysForm(forms.ModelForm):

class KeysForm(forms.Form):
    keys = forms.CharField(label='', max_length=100)

    class Meta:
        model = Keys
        fields = '__all__'

    def clean_keys(self):
        keys = cleaned_data.get('keys')

    # def clean_slug(self):
    #     return self.cleaned_data['slug'].lower()
