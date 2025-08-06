# recipes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    # Esta linha é crucial: define a URL e nomeia ela como 'recipe_detail'
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    # Outras URLs do seu aplicativo...
]
