from django.contrib import admin
from .models import Characters
from .models import Comics

# Register your models here.

admin.site.register(Characters)
admin.site.register(Comics)

