"""backend URL Configuration

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
from django.urls import path, include, re_path

# from rest_framework.authtoken import views
# from rest_framework.authtoken.views import obtain_auth_token 
# # from .router import router
# from rest_framework.authtoken import views
# from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userapp.urls')),
    path('', include('userdetailsapp.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    # path(r'^', include('userapp.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
