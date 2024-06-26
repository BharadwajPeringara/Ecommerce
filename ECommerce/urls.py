"""
URL configuration for ECommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Recommends.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',login_page),
    path("login_page/",login_page,name="login_page"),
    path('login/',login,name='login'),
    path('home_page/',home_page,name='home_page'),
    path('analyse_page/',analyse_page,name='analyse_page'),
    path('result_page/',result_page,name='result_page'),
    path('logout/',logout,name='logout'),
    path('scrape_products/',scrape_products,name='scrape_products'),

]
