from rest_framework.serializers import ModelSerializer

from .models import Pokemon


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'
        extra_kwargs = {
                        'name': {'required': True, 'allow_blank': False},
                        'typePokemon': {'required': True, 'allow_blank': False},
                        'level': {'required': True, },
                        'atack': {'required': True, },
                        'defense': {'required': True, },
                        'health': {'required': True, },
                        }
