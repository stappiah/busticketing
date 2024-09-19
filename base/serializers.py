from base.models import (
    BusStation,
    Driver,
    Bus,
    BusRoute,
    Schedule,
    Reservation,
    Ticket,
    # WorkingDay
)
from rest_framework import serializers
from account.models import Account


class BusSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

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


# class WorkingDaySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WorkingDay
#         fields = ["id", "day"]


class BusStationSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )
    # working_days = WorkingDaySerializer(many=True)

    class Meta:
        model = BusStation
        fields = "__all__"

    def to_representation(self, instance):
        # Convert the comma-separated working days to a list for the API response
        representation = super().to_representation(instance)
        representation["working_days"] = instance.working_days.split(",")
        return representation

    def validate(self, data):
        # Convert the list of working days to a comma-separated string before saving
        if isinstance(data.get("working_days"), list):
            data["working_days"] = ",".join(data["working_days"])
        return data


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Schedule
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Reservation
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
