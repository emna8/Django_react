from rest_framework import serializers
from .models import Person

class PersonSerialiser(serializers.ModelSerializer):

    class Meta:
        model=Person
        fields=('name','age')
        #fields='__all__'  if you want to send all the attributes (password to)



