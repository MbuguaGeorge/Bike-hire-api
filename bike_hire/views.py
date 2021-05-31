from django.shortcuts import render
from rest_framework import serializers, generics, permissions
from .serializers import UserSerializer, ListSerializer, ProfileSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Student,Profile
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

class userlist(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ListSerializer

    def get_queryset(self):
        return Profile.objects.all()

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

    def get(self, request,):
        for user in Student.objects.all():
            token = Token.objects.get(user=user)
            if token:
                return Response({user.username : user.auth_token.key})
            else:
                return Response({"error" : "Wrong credentials"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def profiling(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data = request.data)
        data = {}

        if serializer.is_valid():
            prof = serializer.save()
            data['response'] = 'success'
            data['firstname'] = prof.firstname
            data['lastname'] = prof.lastname
            data['contact'] = prof.contact
            data['hourly'] = prof.hourly
            data['daily'] = prof.daily
        else:
            data = serializer.errors
        return Response(data)