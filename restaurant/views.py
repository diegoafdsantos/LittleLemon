from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] 

def index(request):
    return render(request, 'index.html', {})