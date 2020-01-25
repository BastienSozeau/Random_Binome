from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.binome_index, name='binome_index'),
    url(r'^submit', views.submit, name='submit'),

]
