from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviesListView.as_view()),
    path("reviews/<int:pk>", views.SingleRevView.as_view()),
]
