from rest_framework import generics, permissions, authentication
from .serializers import (
    BusSerializer,
    BusRouteSerializer,
    BusStationSerializer,
    TicketSerializer,
    DriverSerializer,
    ReservationSerializer,
    ScheduleSerializer,
    PaymentSerializer,
    BusRentalSerializer,
    RentalPriceSerializer,
    RentalRequestSerializer,
)
from .models import (
    Bus,
    BusRoute,
    BusStation,
    Ticket,
    Driver,
    Reservation,
    Schedule,
    Payment,
    BusRental,
    RentalPrice,
    RentalRequest,
)
from django.db.models import Q
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


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
        if hasattr(self.request.user, "station") and self.request.user.station:
            station_id = self.request.user.station.id
            queryset = BusStation.objects.filter(
                Q(admin=self.request.user) | Q(id=station_id)
            )
            return queryset
        return BusStation.objects.filter(admin=self.request.user)


class CreateBus(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusSerializer
    queryset = Bus.objects.all()


class RetrieveBusDetail(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusSerializer

    def get_object(self):
        bus_id = self.kwargs.get("pk")
        return get_object_or_404(Bus, id=bus_id)

    def get(self, request, *args, **kwargs):
        # Retrieve the bus object
        bus = self.get_object()

        # Serialize the bus object
        serializer = self.get_serializer(bus)

        # Return the serialized data in the response
        return Response(serializer.data)


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


class ListReservation(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ReservationSerializer

    def get_queryset(self):
        station = self.kwargs.get("pk")
        queryset = Reservation.objects.filter(schedule__station=station)
        return queryset


class CreateSchedule(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()


class RetrieveUpdateDeleteSchedule(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()


class RetrieveScheduleReservation(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ReservationSerializer

    def get_queryset(self):
        schedule_id = self.kwargs.get('pk')
        queryset = Reservation.objects.filter(schedule=schedule_id)
        return queryset


class RetrieveStationSchedule(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        station = self.kwargs.get("pk")
        queryset = Schedule.objects.filter(station=station)
        return queryset


class CreatePayment(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class UserCurrentReservation(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ReservationSerializer

    def get_queryset(self):
        status = "on_going"
        queryset = Reservation.objects.filter(
            user=self.request.user, schedule__status=status
        )
        return queryset


class UserCompletedReservation(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ReservationSerializer

    def get_queryset(self):
        status = "completed"
        queryset = Reservation.objects.filter(
            user=self.request.user, schedule__status=status
        )
        return queryset


class CreateBusRental(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusRentalSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rental = serializer.save()

        return Response(
            {
                "id": rental.pk,
                "station": rental.station.id,
                "phone_number": rental.phone_number,
            }
        )


class ListBusRentals(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusRentalSerializer
    queryset = BusRental.objects.all()


class RetrieveBusRental(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusRentalSerializer
    queryset = BusRental.objects.all()


class GetBusRental(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusRentalSerializer

    def get_queryset(self):
        station = self.kwargs.get("pk")
        queryset = BusRental.objects.filter(station=station)
        return queryset


class DeleteBusRental(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BusRentalSerializer
    queryset = BusRental.objects.all()


class CreateRentalPrice(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = RentalPriceSerializer
    queryset = RentalPrice.objects.all()


class BusRentalPrices(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = RentalPriceSerializer

    def get_queryset(self):
        rental_id = self.kwargs.get("pk")
        queryset = RentalPrice.objects.filter(rental=rental_id)
        return queryset


class CreateRentalRequest(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = RentalRequestSerializer
    queryset = RentalRequest.objects.all()


class StationRentalRequest(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = RentalRequestSerializer

    def get_queryset(self):
        station_id = self.kwargs.get("pk")
        queryset = RentalRequest.objects.filter(rental__station=station_id)
        return queryset


class UserRentalRequest(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = RentalRequestSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = RentalRequest.objects.filter(user=user)
        return queryset
