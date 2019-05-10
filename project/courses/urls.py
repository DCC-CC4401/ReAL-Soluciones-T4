from django.conf.urls import url
from django.contrib import admin
from .import views

app_name='courses'

urlpatterns = [
    url(r'^$', views.courses_list, name="list"),
    url(r'^delete/$', views.delete_course, name='delete_course'),
]
