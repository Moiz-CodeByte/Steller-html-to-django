from . import views
from django.urls import path

urlpatterns = [
    # path('', views.steller, name='steller'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]