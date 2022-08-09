from django.shortcuts import render
from .models import Animal

# Add the Cat class & list and view function below the imports

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def animals_index(request):
  animals = Animal.objects.all()
  return render(request, 'animals/index.html', {'animals' : animals})
  
def animals_detail(request, animal_id):
  animal = Animal.objects.get(id=animal_id)
  return render(request, 'animals/detail.html', { 'animal' : animal})