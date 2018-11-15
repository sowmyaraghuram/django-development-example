from django.conf.urls import url
from learningApp import views

#Template Tagging
app_name = 'learningApp'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
