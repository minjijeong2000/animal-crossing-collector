from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('animals/', views.animals_index, name='animals_index'),
    path('animals/<int:animal_id>/', views.animals_detail, name='animals_detail'),
    path('animals/create/', views.AnimalCreate.as_view(), name='animals_create'),
    path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animals_update'),
    path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animals_delete'),
    path('animals/<int:animal_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('animals/<int:animal_id>/assoc_fruit/<int:fruit_id>/', views.assoc_fruit, name='assoc_fruit'),
    path('fruits/create/', views.FruitCreate.as_view(), name='fruits_create'),
    path('fruits/<int:pk>/', views.FruitDetail.as_view(), name='fruits_detail'),
    path('fruits/', views.FruitList.as_view(), name='fruits_index'),
    path('fruits/<int:pk>/update/', views.FruitUpdate.as_view(), name='fruits_update'),
    path('fruits/<int:pk>/delete/', views.FruitDelete.as_view(), name='fruits_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
