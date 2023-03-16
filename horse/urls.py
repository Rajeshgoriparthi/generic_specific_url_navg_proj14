from django.urls import path
from horse.views import *
app_name='horse'
urlpatterns=[
    path('badsha/',badsha,name='badsha'),
    path('kajal/',kajal,name='kajal'),
]