from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightSerializer , BookingSerializer
from datetime import date


class FlightListView(ListAPIView):
		queryset = Flight.objects.all()
		serializer_class = FlightSerializer

class BookingListView(ListAPIView):
		queryset = Booking.objects.filter(date__gte =date.today())
		serializer_class = BookingSerializer
