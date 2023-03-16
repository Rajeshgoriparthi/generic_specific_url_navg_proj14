from django.urls import path
from tiger.views import *
app_name='tiger'
urlpatterns=[
    path('tiger1/',tiger1,name='tiger1'),
    path('tiger2/',tiger2,name='tiger2'),

]