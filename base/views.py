from rest_framework import generics, permissions, authentication
from .serializers import (
    BusSerializer,
    BusRouteSerializer,
    BusStationSerializer,
    TicketSerializer,
    DriverSerializer,
    ReservationSerializer,
    Ticket,
)
from .models import Bus, BusRoute, BusStation, Ticket, Driver, Reservation, Schedule
from django.db.models import Q


# Create your views here.
class CreateListBusStation(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusStationSerializer
    queryset = BusStation.objects.all()


class RetrieveUpdateDeleteBusStation(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusStationSerializer
    queryset = BusStation.objects.all()


class RetrieveAdminStation(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusStationSerializer

    def get_queryset(self):
        return BusStation.objects.filter(Q(admin=self.request.user) | Q(id=self.request.user.station.id))


class CreateBus(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusSerializer
    queryset = Bus.objects.all()


class DeleteBus(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusSerializer
    queryset = Bus.objects.all()


class GetStationBus(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusSerializer

    def get_queryset(self):
        station = self.kwargs.get("pk")
        queryset = Bus.objects.filter(station=station)
        return queryset


class CreateRoute(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusRouteSerializer
    queryset = BusRoute.objects.all()


class RetrieveUpdateDeleteRoute(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusRouteSerializer
    queryset = BusRoute.objects.all()


class ListRoutes(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusRouteSerializer

    def get_queryset(self):
        station = self.kwargs.get("pk")
        queryset = BusRoute.objects.filter(station=station)
        return queryset


class CreateDriverView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class GetDrivers(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = DriverSerializer

    def get_queryset(self):
        station_id = self.kwargs.get("pk")
        queryset = Driver.objects.filter(station=station_id)
        return queryset


class DeleteDriver(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class CreateTicket(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class RetrieveUpdateDeleteTicket(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class CreateReservation(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


class CreateReservation(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


class ListReservation(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ReservationSerializer

    def get_queryset(self):
        station = self.kwargs.get("pk")
        queryset = Reservation.objects.filter(schedule__station=station)
        return queryset
