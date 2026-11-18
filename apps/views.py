from django.shortcuts import render
from django.views import View

# Create your views here.


class ChatRoomView(View):
    def get(self, request):
        return render(request, 'chat.html')