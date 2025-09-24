from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('home/',views.index ,name='index'),
    path('home/details/<int:id>', views.details, name='details'),
    path('testing',views.testing),
    path('add/', views.add, name='add'),
    path('add_record/', views.add_record, name='add_record'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    
]