from django.contrib import admin
from .models import Animal, Feeding, Fruit

# Register your models here.
admin.site.register(Animal)
admin.site.register(Feeding)
admin.site.register(Fruit)