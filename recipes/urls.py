# recipes/urls.py
from django.urls import path # Importa a função 'path' que define URLs.
from . import views # Importa o arquivo views.py do próprio app.

urlpatterns = [
path('', views.recipe_list, name='recipe_list'), 
path('<int:pk>/', views.recipe_detail, name='recipe_detail')

]