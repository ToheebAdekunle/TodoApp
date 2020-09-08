from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('update_stuff/<str:pk>/', views.updateStuff, name="update_stuff"),
    path('delete_stuff/<str:pk>/', views.deleteStuff, name="delete_stuff")
]