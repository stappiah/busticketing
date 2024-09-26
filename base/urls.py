from django.urls import path
from . import views

urlpatterns = [
    path("create-bus-station", views.CreateListBusStation.as_view()),
    path("bus-station-details/<int:pk>", views.RetrieveUpdateDeleteBusStation.as_view()),
    path("admin-station", views.RetrieveAdminStation.as_view()),

    path("create-bus", views.CreateBus.as_view()),
    path("delete-bus/<int:pk>", views.DeleteBus.as_view()),
    path("get-bus/<int:pk>", views.RetrieveBusDetail.as_view()),
    path("station-bus/<int:pk>", views.GetStationBus.as_view()),

    path("create-bus-route", views.CreateRoute.as_view()),
    path("bus-route-details/<int:pk>", views.RetrieveUpdateDeleteRoute.as_view()),
    path("station-routes/<int:pk>", views.ListRoutes.as_view()),

    path("create-driver", views.CreateDriverView.as_view()),
    path("get-driver/<int:pk>", views.GetDrivers.as_view()),
    path("delete-driver/<int:pk>", views.DeleteDriver.as_view()),

    path("create-ticket", views.CreateTicket.as_view()),
    path("ticket-details/<int:pk>", views.RetrieveUpdateDeleteTicket.as_view()),

    path("create-reservation", views.CreateReservation.as_view()),
    path("station-reservation/<int:pk>", views.ListReservation.as_view()),
    path("create-payment", views.CreatePayment.as_view()),
    path("user-reservation", views.UserCurrentReservation.as_view()),

    path("schedule", views.CreateSchedule.as_view()),
    path("schedule/<int:pk>", views.RetrieveUpdateDeleteSchedule.as_view()),
    path("station-schedule/<int:pk>", views.RetrieveStationSchedule.as_view()),

    path("bus-rental", views.CreateBusRental.as_view()),
    path("list-bus-rental", views.ListBusRentals.as_view()),
    path("delete-bus-rental/<int:pk>", views.DeleteBusRental.as_view()),
    path("station-bus-rental/<int:pk>", views.GetBusRental.as_view()),

    path("rental-price", views.CreateRentalPrice.as_view()),
    path("bus-rental-prices/<int:pk>", views.BusRentalPrices.as_view()),

    path("rental-request", views.CreateRentalRequest.as_view()),

]
