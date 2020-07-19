from rest_framework.serializers import ModelSerializer
from .models import Pokemon


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['__all__']
