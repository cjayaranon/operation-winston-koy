from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.views.generic import View

class AboutView(View):

    def get(self, request):
        return render(request, "about.html")

def bootstrap_trial(request):
    return render(request, 'bootstrap_trial.html')