from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.notelist),
    path('notes/<int:pk>', views.detail),
]