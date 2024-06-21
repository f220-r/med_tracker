from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('home/', views.home, name='home'),
    path('log-in/', views.signin, name='sign_in'),
    path('equipments/', views.equipments, name='equipments'),
]