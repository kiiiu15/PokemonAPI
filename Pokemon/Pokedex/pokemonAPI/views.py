from django.shortcuts import render
from .models import Pokemon
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view()
def index(request):
    pokemon_list = Pokemon.objects.all()
    return Response(pokemon_list)
