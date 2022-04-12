from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homePage'),
    path('detail/<int:id>', detail_view , name="post_detail"),
    path('services/', services, name='servicePage'),
    path('offers/', offers, name='offerPage'),
    path('contact/', contact, name='contactPage'),
    path('booking', booking, name='bookingPage'),
    path('dash/', dashboard, name='adminPage')
]
