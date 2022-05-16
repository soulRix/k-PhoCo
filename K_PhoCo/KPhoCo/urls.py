from django.urls import path
from . import views # '.' means current directory

urlpatterns = [
    path('', views.home, name = "KPhoCo"), #views is the name of the File, and the '.home' is the name of the function
    path('about/', views.about, name = "KPhoCo-about"),
]
