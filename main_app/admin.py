from django.contrib import admin
from .models import Animal, Feeding, Toy

# Register your models here.
admin.site.register(Animal)
admin.site.register(Feeding)
admin.site.register(Toy)