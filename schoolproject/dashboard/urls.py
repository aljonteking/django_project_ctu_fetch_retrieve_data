from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This is your home view
    # Add more paths for other views in your app
]
