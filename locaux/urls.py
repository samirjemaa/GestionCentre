from django.urls import path

from locaux import views

urlpatterns = [
    path('', views.home, name="home_locaux"),
    path('add_local/', views.add_local, name="add_locaux"),
]
