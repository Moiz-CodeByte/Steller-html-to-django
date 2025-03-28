from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def steller(request):
    return HttpResponse("Hello world!")
def home(request): 
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')
def blog(request):
    return render(request, 'blog.html')
def portfolio(request): 
    return render(request, 'portfolio.html')
def testimonials(request):
    return render(request, 'testimonials.html')