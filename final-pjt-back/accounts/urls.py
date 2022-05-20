from django.urls import path
from . import views


# accounts/

urlpatterns = [
    
    path('profile/<str:username>/', views.profile),
    path('profile/<str:username>/follow/', views.follow),
    path('profile/<str:username>/watched/', views.watched),
]
