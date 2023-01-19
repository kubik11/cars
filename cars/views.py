from django.shortcuts import render
from .models import Team
# Create your views here.
def home(request):
	data = Team.objects.all()
	team = {
		'teams': data
	}
	return render(request, 'pages/home.html', team)
def about(request):
	data = Team.objects.all()
	team = {
		'teams': data
	}
	return render(request, 'pages/about.html', team)
def cars(request):
	return render(request, 'pages/cars.html')
def services(request):
	return render(request, 'pages/services.html')
def contact(request):
	return render(request, 'pages/contact.html')