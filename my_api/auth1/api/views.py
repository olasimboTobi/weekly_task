from rest_framework.decorators import api_view
from rest_framework.response import Response
from auth1.api.serializers import RegistrationSerializer
# from rest_framework.authtoken.models import Token
from rest_framework import status


# from auth1 import models




@api_view(['POST',])
def registration_view(request):


    if request.method == 'POST':
        serializer = RegistrationSerializer(data =request.data)

        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)