from django.shortcuts import render, get_object_or_404
from .models import Rooms, Users

# Create your views here.

def room_list(request):
    rooms = Rooms.objects.order_by('-EnterDate')
    return render(request, 'hotel/room_list.html', {'rooms':rooms})

def room_detail(request, pk):
    room = get_object_or_404(Rooms, pk=pk)
    return render(request, 'hotel/room_detail.html', {'room': room})
