from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.ItineraryList.as_view()),
    path('users/<int:pk>/', views.ItineraryDetail.as_view()),
]
