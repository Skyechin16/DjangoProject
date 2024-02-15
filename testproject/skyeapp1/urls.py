from django.urls import path
from skyeapp1 import views
urlpatterns=[
    path('',views.index),
    path('about',views.about),
    path('gallery',views.gallery)
]