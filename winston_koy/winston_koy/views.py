from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.views.generic import View


class AboutView(View):

    def get(self, request):
        return render(request, "about.html")

def trainers_page(request):
    return render(request, 'trainers.html')

def trainer_profile(request):
    return render(request, 'course_trainer_profile.html')

def contact_page(request):
    return render(request, 'contact_us.html')
