from .forms import KeysForm
from django.shortcuts import render
from django.template import loader
# from django.conf.urls import patterns, include, url
from django.views.generic import *
from django.http import HttpResponseRedirect
from django import forms


def main(request):
    return render(request,'index.html')

def thanks(request):
    return render(request, 'thanks.html')

def get_keys(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = KeysForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('zlou/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = KeysForm()

    return render(request, 'index.html', {'form': form})



