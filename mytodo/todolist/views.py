from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.template import loader

from .models import Category, TodoListItem
# Create your views here.

def index(request):
    """This is jus the index page go show stuff"""
    latest_category_list = Category.objects.all()
    context = {
        "latest_cat_list" : latest_category_list,
        }

    return render(request, "todolist/index.html", context)

def create_category(request):
    """ This allows users to create a category for which todo items will be added """
    pass

def view_category(request, category_id):
    """ This allows users to view items under each category"""
    category_id = int(category_id)
    category = Category.objects.get(pk=category_id)
    name = category.cat_name
    todoItems = TodoListItem.objects.filter(category = category)
    context = {
        "items": todoItems,
        "category": name,
        "id": category_id
    }
    return render(request, "todolist/category.html", context)

def add_item(request, category_id):
    """ This allows the user to add an item to a specific category"""
    if request.method == "POST":
        id = int(category_id)
        category = Category.objects.get(pk=id)
        item = request.POST["item"]
        the_item =TodoListItem(item=item, category = category)
        the_item.save()
        return HttpResponseRedirect(reverse("category", args=(id,)))
 