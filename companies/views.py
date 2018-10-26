from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerialiser


@api_view(['GET'])
def person_list(request):
    #/persons
    if request.method == 'GET':
        snippets = Person.objects.all()
        serializer = PersonSerialiser(snippets, many=True)
        return Response(serializer.data)

