from base.models import (
    BusStation,
    Driver,
    Bus,
    BusRoute,
    Schedule,
    Reservation,
    Ticket,
    Payment,
    BusRental,
    RentalPrice,
    RentalRequest,
)
from rest_framework import serializers
from account.models import Account


class BusSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )
    station_address = serializers.ReadOnlyField()

    class Meta:
        model = Bus
        fields = "__all__"


class BusRouteSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = BusRoute
        fields = "__all__"


class BusStationSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = BusStation
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )
    get_destination = serializers.ReadOnlyField()
    seat_number = serializers.ReadOnlyField()
    car_number = serializers.ReadOnlyField()
    get_station = serializers.ReadOnlyField()
    gear_type = serializers.ReadOnlyField()
    fuel_type = serializers.ReadOnlyField()
    station_address = serializers.ReadOnlyField()

    class Meta:
        model = Schedule
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )
    get_amount = serializers.ReadOnlyField()
    get_destination = serializers.ReadOnlyField()
    get_car_number = serializers.ReadOnlyField()

    class Meta:
        model = Reservation
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Payment
        fields = "__all__"


class BusRentalSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )
    get_bus_image = serializers.ReadOnlyField()
    get_station_name = serializers.ReadOnlyField()
    get_bus_name = serializers.ReadOnlyField()
    get_car_number = serializers.ReadOnlyField()

    class Meta:
        model = BusRental
        fields = "__all__"


class RentalPriceSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = RentalPrice
        fields = "__all__"


class RentalRequestSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = RentalRequest
        fields = "__all__"
