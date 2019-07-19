from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
# url('', views.mysum)
path('sum/<slug:nubmers>/',views.mysum),
path('list1/', views.list1),
path('list2/', views.list2),
path('list3/', views.list3),
]