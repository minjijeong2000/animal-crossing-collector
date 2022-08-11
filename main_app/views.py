from ast import List
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal, Fruit
from .forms import FeedingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

# Add the Cat class & list and view function below the imports
class Home(LoginView):
  template_name = 'home.html'
  
class AnimalCreate(LoginRequiredMixin, CreateView):
  model = Animal
  fields = ['name', 'breed', 'description', 'age']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  success_url = '/animals/'
  
class AnimalUpdate(UpdateView):
  model = Animal
  fields = ['breed', 'description', 'age']
  
class AnimalDelete(DeleteView):
  model = Animal
  success_url = '/animals/'
  
class FruitCreate(CreateView):
  model = Fruit
  fields = '__all__'
  
class FruitList(ListView):
  model = Fruit
  
class FruitDetail(DetailView):
  model = Fruit
  
class FruitUpdate(UpdateView):
  model = Fruit
  fields = ['name', 'color']
  
class FruitDelete(DeleteView):
  model = Fruit
  success_url = '/fruits/'

# Create your views here.
# def home(request):
#   return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def animals_index(request):
  animals = Animal.objects.filter(user=request.user)
  return render(request, 'animals/index.html', {'animals' : animals})
  
def animals_detail(request, animal_id):
  animal = Animal.objects.get(id=animal_id)
  fruits_animal_doesnt_have = Fruit.objects.exclude(id__in = animal.fruits.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'animals/detail.html', { 'animal' : animal, 'feeding_form' : feeding_form, 'fruits': fruits_animal_doesnt_have})

def add_feeding(request, animal_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.animal_id = animal_id
    new_feeding.save()
  return redirect('animals_detail', animal_id=animal_id)

def assoc_fruit(request, animal_id, fruit_id):
  Animal.objects.get(id=animal_id).fruits.add(fruit_id)
  return redirect('animals_detail', animal_id=animal_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('animals_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message' : error_message}
  return render (request, 'signup.html', context)