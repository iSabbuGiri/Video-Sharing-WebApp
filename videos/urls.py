from django.contrib import admin
from django.urls import path
from .views import CreateVideo

urlpatterns = [
    path('create/',CreateVideo.as_view(), name='video-create' ),
]
