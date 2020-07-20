from django.db import models
import json


# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=30, default='No name')
    typePokemon = models.CharField(max_length=30, default='No type')
    level = models.IntegerField(default=1)
    atack = models.IntegerField(default=1)
    defense = models.IntegerField(default=1)
    health = models.IntegerField(default=100)



    def __str__(self):
        return '{"name" : "%s" ,' \
               ' "typePokemon" : "%s" ,' \
               ' "level" : %d ,' \
               ' "atack" : %d,' \
               ' "defense" : %d,' \
               '"health" : %d}' % (self.name, self.typePokemon, self.level, self.atack, self.defense, self.health)


