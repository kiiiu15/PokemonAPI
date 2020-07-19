from django.db import models


# Create your models here.


class Pokemon(models.Model):
    typePokemon = models.CharField(max_length=30, default='No type')
    level = models.IntegerField(default=1)
    atack = models.IntegerField(default=1)
    defense = models.IntegerField(default=1)
    health = models.IntegerField(default=100)
