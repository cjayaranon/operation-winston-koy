"""winston_koy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import AboutView

admin.autodiscover()

from .views import trainers_page, trainer_profile, contact_page


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', TemplateView.as_view(template_name='about.html')),
    url(r'^trainers_page/', trainers_page),
    url(r'^trainers/$', trainer_profile),
    url(r'contact_us/', contact_page),
)
