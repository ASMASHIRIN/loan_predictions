from django.urls import path
from appname import views

urlpatterns = [
    path('home/', views.home, name='home'),
]
