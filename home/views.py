from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views = {}
    views['about_me'] = AboutMe.objects.all()
    views['services'] = Service.objects.all()
    views['feedbacks'] = Feedback.objects.all()
    return render(request,'index.html',views)


def about(request):
    views = {}
    views['feedbacks'] = Feedback.objects.all()
    return render(request,'about.html',views)

def contact(request):
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    return render(request,'price.html')

def services(request):
    views = {}
    views['services'] = Service.objects.all()
    views['feedbacks'] = Feedback.objects.all()
    return render(request,'services.html',views)