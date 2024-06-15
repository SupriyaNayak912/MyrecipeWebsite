from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/new/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
    path('recipe/<int:pk>/comment/', views.add_comment_to_recipe, name='add_comment_to_recipe'),
    path('recipe/<int:pk>/rating/', views.add_rating_to_recipe, name='add_rating_to_recipe'),
    path('search/', views.search_recipes, name='search_recipes'),
]
