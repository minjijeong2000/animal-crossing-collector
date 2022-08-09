from django.shortcuts import render
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Animal:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

animals = [
  Animal('Lolo', 'tabby', 'Kinda rude.', 3),
  Animal('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Animal('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Animal('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')

def animals_index(request):
    return render(request, 'animals/index.html', {'animals' : animals})