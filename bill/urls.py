from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL pattern for the index view
    path('print/', views.print, name='customer_details'),  # URL pattern for the print view
    path('login/', views.login, name='login'),  # URL pattern for the login view
]
