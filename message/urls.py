from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('message_input/', views.message_input, name='message_input'),
]