from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader

from .models import Category, TodoListItem
# Create your views here.

def index(request):
    """This is jus the index page go show stuff"""
    latest_category_list = Category.objects.all()
    output = "\n,".join([category.cat_name for category in latest_category_list])
    context = {
        "latest_cat_list" : latest_category_list,
        }

    return render(request, "todolist/index.html", context)

def create_category(request):
    """ This allows users to create a category for which todo items will be added """
    pass

def view_category(request, category_id):
    """ This allows users to view items under each category"""
    pass

def add_item(request, category_id):
    """ This allows the user to add an item to a specific category"""
    pass
