from django.shortcuts import render
from rest_framework import serializers, generics, permissions
from .serializers import UserSerializer, ListSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Student
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status

# Create your views here.

@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def registration(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "success"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)

class userlist(generics.ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = ListSerializer

    def get_queryset(self):
        return Student.objects.all()

@permission_classes((permissions.AllowAny,))
class TokenView(APIView):
    def post(self,request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({"token" : user.auth_token.key})
        else:
            return Response({"error" : "Wrong credentials"}, status = status.HTTP_400_BAD_REQUEST)