"""wehireproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import *
from wehireapp import views

urlpatterns = [

    path('',views.index),
    path('login/',views.login),
    # path('register/',views.register),
    # path('postjob/',views.postJob),
    path('token/',views.token),
    path('regis/',views.regis),
    path('verify/<auth_token>',views.verify),
    path('error/',views.error),
    path('companylogin/',views.compProfile),
    path('postjob/',views.post_job),
    path('registeredcompanies/',views.registeredcompanies),
    path('editprofile/<str:username>/<str:token>',views.editprofile),
    path('jobdisplay/',views.postdisplay),
    path('userlogin/',views.userlogin),
    path('userregister/',views.userregister),
    path('readmore/<int:id>',views.readmore),
    path('apply/<str:title>/<str:company_name>',views.apply),
    path('jobs_by_company/<str:cname>',views.companyjobs),
    path('view_applicants/<str:companyname>/<str:title>',views.viewapplicants)









]


