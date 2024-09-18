from django.db import models
from django.conf import settings

# Create your models here.
"""
TODO
 bus route, passenger, booking, ticket,
"""


LOCATION_REGION = [
    ("Upper West Region", "Upper West Region"),
    ("Upper East Region", "Upper East Region"),
    ("North East Region", "North East Region"),
    ("Northern Region", "Northern Region"),
    ("Savannah Region", "Savannah Region"),
    ("Bono East Region", "Bono East Region"),
    ("Brong Ahafo Region", "Brong Ahafo Region"),
    ("Oti Region", "Oti Region"),
    ("Volta Region", "Volta Region"),
    ("Eastern Region", "Eastern Region"),
    ("Ashanti Region", "Ashanti Region"),
    ("Ahafo Region", "Ahafo Region"),
    ("Western North Region", "Western North Region"),
    ("Western Region", "Western Region"),
    ("Central Region", "Central Region"),
    ("Greater Accra Region", "Greater Accra Region"),
]

BOOKING_STATUS = [
    ("on_going", "On going"),
    ("completed", "Completed"),
]

WORKING_DAYS_CHOICES = [
    ("MON", "Monday"),
    ("TUE", "Tuesday"),
    ("WED", "Wednesday"),
    ("THU", "Thursday"),
    ("FRI", "Friday"),
    ("SAT", "Saturday"),
    ("SUN", "Sunday"),
]

GEAR_TYPE = [
    ("manual", "Manual"),
    ("auto", "Automatic"),
]

FUEL_TYPE = [
    ("diesel", "Diesel"),
    ("petrol", "Petrol"),
]


class WorkingDay(models.Model):
    day = models.CharField(max_length=3, choices=WORKING_DAYS_CHOICES, unique=True)

    def __str__(self):
        return dict(WORKING_DAYS_CHOICES)[self.day]


class BusStation(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    station_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    region = models.CharField(
        choices=LOCATION_REGION, max_length=20, blank=True, null=True
    )
    image = models.ImageField(upload_to="images", null=True, blank=True)
    working_days = models.ManyToManyField(WorkingDay, related_name="station")
    start_time = models.TimeField()
    closing_time = models.TimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.station_name


class Driver(models.Model):
    station = models.ForeignKey(BusStation, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    license_id = models.CharField(max_length=50)


class Bus(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    station = models.ForeignKey(BusStation, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=100, null=True, blank=True)
    car_number = models.CharField(max_length=20)
    seat_number = models.IntegerField()
    air_conditioner = models.BooleanField(default=False)
    fuel_type = models.CharField(max_length=6, choices=FUEL_TYPE, default="diesel")
    gear_type = models.CharField(max_length=9, choices=GEAR_TYPE, default="manual")
    bus_image = models.ImageField(upload_to="images", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.station.station_name} bus number {self.car_name}"


class BusRoute(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    station = models.ForeignKey(
        BusStation, on_delete=models.PROTECT, related_name="bus_origin"
    )
    route_name = models.CharField(max_length=100)
    region = models.CharField(
        choices=LOCATION_REGION, max_length=20, blank=True, null=True
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Route from {self.origin} to {self.destination}"


class Schedule(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    station = models.ForeignKey(BusStation, on_delete=models.PROTECT)
    destination = models.ForeignKey(BusRoute, on_delete=models.PROTECT)
    bus = models.ForeignKey(Bus, on_delete=models.PROTECT)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=9, choices=BOOKING_STATUS)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bus from {self.station.station_name} to {self.destination.route_name}"


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    status = models.CharField(max_length=12, choices=BOOKING_STATUS)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Ticket(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ticket number {self.pk}"
