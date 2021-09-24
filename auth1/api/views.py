from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from auth1.api.serializers import RegistrationSerializer
from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from django_otp.oath import hotp
from django.core.exceptions import ObjectDoesNotExist
from auth1 import models
# from django.core.mail import send_email

@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == 'GET':
        request.user.auth_token.delete()
        return Response({"success": ("Successfully logged out.")}, status=status.HTTP_200_OK)
    # try:
    #     request.user.auth_token.delete()
    # except (AttributeError, ObjectDoesNotExist):
    #     pass

    # logout_view(request)

    # return Response({"success": _("Successfully logged out.")},
    #                 status=status.HTTP_200_OK)
# def logout_view(request):
#     if request.method == 'POST':
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)





@api_view(['POST',])
@permission_classes([AllowAny])
def registration_view(request):
   

    if request.method == 'POST':
        serializer = RegistrationSerializer(data =request.data)
        data = {}

        if  serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration Successful"
            data['username'] = account.username
            data['email'] = account.email
            # token = Token.objects.get(user=account).key
            # data['token'] = token
            data['otp'] = create_otp(key= b'1234567890123467890',counter=2, digit=6)
            # send_email(data['otp'])

            return Response(data)
        else:
            return Response(serializer.errors)





def create_otp(key, counter, digit):
    secret_key = b'1234567890123467890'
    for counter in range(5):
        return(hotp(key=secret_key,counter=counter,digits=6))