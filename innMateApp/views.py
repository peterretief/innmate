from django.shortcuts import render
from .models import Guest
# Create your views here.

def guest_list(request):
    guests = Guest.objects.order_by('published_date')
    return render(request, 'guests/guest_list.html', {"guests": guests})
