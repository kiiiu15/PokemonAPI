from django.urls import path
from . import views
app_name = 'pokemonAPI'
urlpatterns = [
    path('pokemon/', views.PokemonList.as_view()),
    path('pokemon/<int:pk>/', views.PokemonDetail.as_view())
]
