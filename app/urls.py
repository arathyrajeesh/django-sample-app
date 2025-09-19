from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('home/',views.index ),
    path('home/details/<int:id>', views.details, name='details'),
    path('testing',views.testing)
]