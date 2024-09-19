from django.urls import path
from . import views

urlpatterns = [
    path("create-bus-station", views.CreateListBusStation.as_view()),
    path("bus-station-details/<int:pk>", views.RetrieveUpdateDeleteBusStation.as_view()),
    path("admin-station", views.RetrieveAdminStation.as_view()),

    path("create-bus", views.CreateBus.as_view()),
    path("delete-bus/<int:pk>", views.DeleteBus.as_view()),
    path("station-bus/<int:pk>", views.GetStationBus.as_view()),

    path("create-bus-route", views.CreateRoute.as_view()),
    path("bus-route-details/<int:pk>", views.RetrieveUpdateDeleteRoute.as_view()),
    path("station_routes/<int:pk>", views.ListRoutes.as_view()),

    path("create-driver", views.CreateDriverView.as_view()),
    path("get-driver/<int:pk>", views.GetDrivers.as_view()),
    path("delete-driver/<int:pk>", views.DeleteDriver.as_view()),

    path("create-ticket", views.CreateTicket.as_view()),
    path("ticket-details/<int:pk>", views.RetrieveUpdateDeleteTicket.as_view()),

    path("create-reservation", views.CreateReservation.as_view()),
    path("station-reservation", views.ListReservation.as_view()),

]
