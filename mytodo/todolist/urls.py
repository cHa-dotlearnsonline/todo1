from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("/category/<int:category_id>", views.view_category, name="category"),
    path("/add/<int:category_id>", views.add_item, name="add")
    ]
