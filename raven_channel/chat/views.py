# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    """chat page index"""
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    """room view"""
    info_dict = dict(room_name_json=mark_safe(json.dumps(room_name)))

    return render(request,
                  'chat/room.html',
                  info_dict)
