"""clinicalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

app_name='clinicalsApp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.PatientListView.as_view(),name='PatientListView'),
    path('create',views.PatientCreateView.as_view(),name='PatientCreateView'),
    path('update/<int:pk>',views.PatientUpdateView.as_view(),name='PatientUpdateView'),
    path('delete/<int:pk>',views.PatientDeleteView.as_view(),name="PatientDeleteView"),
    path('addData/<int:pk>',views.addClinicalData,name='AddClinicalData'),
    path('analyze/<int:pk>',views.analyze,name='Analyze'),
]
