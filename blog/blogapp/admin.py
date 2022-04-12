from django.contrib import admin
from blogapp.models import *

# Register your models here.


admin.site.register(Blog)
admin.site.register(Tags)
admin.site.register(Category)