from django.db import models
from django.conf import settings

# Create your models here.

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

BOOLEAN_TYPE = [
    ("yes", "Yes"),
    ("no", "No"),
]


class BusStation(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    station_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    region = models.CharField(
        choices=LOCATION_REGION, max_length=20, blank=True, null=True
    )
    image = models.ImageField(upload_to="images", null=True, blank=True)
    working_days = models.JSONField()
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
    date_created = models.DateTimeField(auto_now_add=True)


class Bus(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    station = models.ForeignKey(BusStation, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=100, null=True, blank=True)
    car_number = models.CharField(max_length=20)
    seat_number = models.IntegerField()
    air_conditioner = models.CharField(max_length=3, choices=BOOLEAN_TYPE, default="no")
    fuel_type = models.CharField(max_length=6, choices=FUEL_TYPE, default="diesel")
    gear_type = models.CharField(max_length=9, choices=GEAR_TYPE, default="manual")
    bus_image = models.ImageField(upload_to="images", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.station.station_name} bus number {self.car_name}"

    def station_address(self):
        return self.station.address

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
        return f"Route from {self.station.address} to {self.route_name}"


class Schedule(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    station = models.ForeignKey(BusStation, on_delete=models.CASCADE)
    destination = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    departure_date = models.DateField()
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=9, choices=BOOKING_STATUS)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bus from {self.station.station_name} to {self.destination.route_name}"

    @property
    def get_destination(self):
        return self.destination.route_name

    @property
    def seat_number(self):
        return self.bus.seat_number

    @property
    def car_number(self):
        return self.bus.car_number

    @property
    def get_station(self):
        return self.station.station_name

    @property
    def gear_type(self):
        return self.bus.gear_type

    @property
    def fuel_type(self):
        return self.bus.fuel_type

    @property
    def station_address(self):
        return self.station.address


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def get_amount(self):
        return self.schedule.amount

    @property
    def get_destination(self):
        return self.schedule.destination.route_name

    @property
    def get_car_number(self):
        return self.schedule.bus.car_number


class Ticket(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ticket number {self.pk}"


class BusRental(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    station = models.ForeignKey(BusStation, on_delete=models.CASCADE)  
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def get_bus_image(self):
        return self.bus.bus_image.url

    @property
    def get_station_name(self):
        return self.station.station_name

    @property
    def get_bus_name(self):
        return self.bus.car_name

    @property
    def get_car_number(self):
        return self.bus.car_number


class RentalPrice(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    destination = models.CharField(choices=LOCATION_REGION, max_length=20)
    rental = models.ForeignKey(BusRental, on_delete=models.CASCADE)


class RentalRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    pickup = models.CharField(max_length=100)
    region = models.CharField(choices=LOCATION_REGION, max_length=20)
    destination = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    rental = models.ForeignKey(BusRental, on_delete=models.PROTECT)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
