from django.shortcuts import render
from .models import Pokemon
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from .serializers import PokemonSerializer


# Create your views here.

class PokemonList(ListCreateAPIView):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        return Pokemon.objects.all()


# @api_view()
# def index(request):
#     pokemon_list = Pokemon.objects.all()
#     return Response(pokemon_list)
