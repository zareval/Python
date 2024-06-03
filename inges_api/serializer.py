from inges_api.models import  persona,pelicula,serie
from rest_framework import serializers

class persona_serializer(serializers.ModelSerializer):
    class Meta:
        model=persona
        fields=['id','nombre','nacionalidad','f_nacimiento','biografia']


class pelicula_serializer(serializers.ModelSerializer):
    class Meta:
        model=pelicula
        fields=['id', 'nombre', 'genero', 'duracion', 'pais', 'f_estreno', 'trailer', 'e_produccion', 'poster']

class serie_serializer(serializers.ModelSerializer):
    class Meta:
        model=serie
        fields=['id', 'nombre', 'genero', 'duracion', 'pais', 'f_estreno', 'trailer', 'e_produccion', 'poster']

