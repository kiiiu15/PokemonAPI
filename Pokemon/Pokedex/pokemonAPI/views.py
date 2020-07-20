from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Pokemon
from .serializers import PokemonSerializer


# Create your views here.

class PokemonList(ListCreateAPIView):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        return Pokemon.objects.all()


class PokemonDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        return Pokemon.objects.all()
