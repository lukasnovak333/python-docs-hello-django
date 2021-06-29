from django.urls import path

from . import views, services

urlpatterns = [    
    path('', views.hello, name='hello'),
    path('services/postTestResult', services.single_service, name='service')
]
