

from django.urls import path
from .views import Home,Contact


urlpatterns = [

    path('',Home, name='home-page'),
    path('Contact',Contact, name='contact-page')

]