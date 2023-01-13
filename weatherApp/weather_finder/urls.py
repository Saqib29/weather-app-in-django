from django.urls import path
from weather_finder import views

app_name = 'weather_finder'

urlpatterns = [
    path('', views.index, name="index-search"),
    # path('<str:city>/', views.index, name='index'),
]
