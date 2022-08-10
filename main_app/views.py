from ast import List
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal, Toy
from .forms import FeedingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView

# Add the Cat class & list and view function below the imports
class AnimalCreate(CreateView):
  model = Animal
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/animals/'
  
class AnimalUpdate(UpdateView):
  model = Animal
  fields = ['breed', 'description', 'age']
  
class AnimalDelete(DeleteView):
  model = Animal
  success_url = '/animals/'
  
class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'
  
class ToyList(ListView):
  model = Toy
  
class ToyDetail(DetailView):
  model = Toy
  
class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']
  
class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

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
  toys_animal_doesnt_have = TOy.objects.exclude(id__in = animal.toys.all().values_lsit('id'))
  feeding_form = FeedingForm()
  return render(request, 'animals/detail.html', { 'animal' : animal, 'feeding_form' : feeding_form, 'toys': toys_animal_doesnt_have})

def add_feeding(request, animal_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.animal_id = animal_id
    new_feeding.save()
  return redirect('animals_detail', animal_id=animal_id)

def assoc_toy(request, animal_id, toy_id):
  Toy.objects.get(id=animal_id).toys.add(toy_id)
  return redirect('animals_detail', animal_id=animal_id)