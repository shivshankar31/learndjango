from django.urls import path
from .import views

# convert the path to string and integer, to handle both.

urlpatterns = [
    path('', views.index), # empty path will generate "/challenges/"  
    path('<int:month>', views.monthly_challenge_as_int),
    path('<str:month>', views.monthly_challenges,  name='challanges_urlpath') #name is used to specify in reverse()
]
