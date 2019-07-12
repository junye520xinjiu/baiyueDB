from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^about/', views.about),
    url(r'^search/', views.search_form,name='search_form'),
    url(r'^detail/(?P<link>.*?)$', views.detail),
]
