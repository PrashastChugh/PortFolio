from django.contrib import admin
from django.urls import path, include
from home import views

#Django admin header customisation

admin.site.site_header = "Developer Donnie"
admin.site.site_title = "Welcome to Donnie's Dashboard"
admin.site.index_title = "Welcome to this portal"


urlpatterns = [
    path('', views.home,name = 'home'),
    path('about', views.about,name = 'about'),
    path('project', views.project,name = 'project'),
    path('contact', views.contact,name = 'contact'),
]
