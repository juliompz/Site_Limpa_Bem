from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing_Page, name='landing-page')
]