from django.contrib import admin
from .models import  Category, TodoListItem
# Register your models here.

admin.site.register(Category)
admin.site.register(TodoListItem)
