from django.contrib import admin

# Register your models here.
from .models import ToDoItem, ToDoList

@admin.register(ToDoList, ToDoItem)
class ToDoAdmin(admin.ModelAdmin):
    pass
