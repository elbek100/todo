from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='home'),
    path('todo', TodoTemplateView.as_view(),name= 'todo')
]