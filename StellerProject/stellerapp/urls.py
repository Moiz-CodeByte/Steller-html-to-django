from . import views
from django.urls import path

urlpatterns = [
    path('', views.steller, name='steller'),
    path('home/', views.home, name='home')
]