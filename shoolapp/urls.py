
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('facts/', views.facts, name='facts'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('application/', views.application, name='application'),
    path('sports/', views.sports, name='sports'),
    path('accomodation/', views.accomodation, name='accomodation'),
]
