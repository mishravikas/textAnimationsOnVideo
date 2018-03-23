from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('<int:video_id>/', views.video, name='video'),
        path('<int:video_id>/animations/', views.animations, name='animations'),
        ]
