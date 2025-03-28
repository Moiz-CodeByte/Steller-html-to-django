from . import views
from django.urls import path

urlpatterns = [
    # path('', views.steller, name='steller'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('testimonials/', views.testimonials, name='testimonials'),
]