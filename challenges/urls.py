from django.urls import path
from .import views


urlpatterns = [
    path('january', views.january),
    path('february', views.february),
    path('march', views.march)
]
