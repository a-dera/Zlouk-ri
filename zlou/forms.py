#...
from .models import Words
from django import forms
# from django.template.defaultfilters import slugify

#class KeysForm(forms.ModelForm):

class WordsForm(forms.Form):
    words = forms.CharField(max_length=50)

    #class Meta:
       # model = Words
        #fields = '__all__'

    #def clean_words(self):
        #words = cleaned_data.get('words')

    # def clean_slug(self):
    #     return self.cleaned_data['slug'].lower()
