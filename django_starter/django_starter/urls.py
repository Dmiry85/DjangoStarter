"""django_starter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('less_1/', include('less_1.urls')),
    path('less_2/', include('less_2.urls')),
    path('less_3/', include('less_3.urls')),
    path('less_4/', include('less_4.urls')),
    path('less_5/', include('less_5.urls')),
    path('less_6/', include('less_6.urls')),
    path('less_8/', include('less_8.urls')),
    path('less_9/', include('less_9.urls')),
    path('less_10/', include('less_10.urls')),
    path('admin/', admin.site.urls),
]
