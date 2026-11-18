
from django.contrib import admin
from django.urls import path
from apps.views import ChatRoomView


urlpatterns = [
    path('', ChatRoomView.as_view(), name='chat_room'),
]
