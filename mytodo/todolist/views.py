from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, World. You are now at the ToDo List homepage")

def create_category(request):
    """ This allows users to create a category for which todo items will be added """
    pass

def view_category(request, category_id):
    """ This allows users to view items under each category"""
    pass

def add_item(request):

    pass
