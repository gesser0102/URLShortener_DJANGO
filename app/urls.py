from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('sucess/<str:url>', views.Redirect, name='redirect')
]

