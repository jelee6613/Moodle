from django.urls import path
from . import views


# accounts/

urlpatterns = [
    
    path('<str:username>/', views.profile),
    path('<str:username>/follow/', views.follow),
    path('<str:username>/watched/', views.watched),
]
