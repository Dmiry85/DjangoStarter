from django.urls import path
from less_1 import views


urlpatterns = [
    path('', views.index, name='index'),
]
