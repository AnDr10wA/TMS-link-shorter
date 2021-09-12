from django.contrib import admin
from django.urls import path
from .views import input_link, relink
urlpatterns = [
    path('', input_link ),
    path('<data>', relink )

]