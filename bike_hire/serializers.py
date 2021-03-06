from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Profile

class UserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    class Meta:
        model = Student
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password' : {'write_only' : True} 
        }
    def save(self):
        user = Student(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'passwords must match'})
        user.set_password(password)
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('firstname','lastname','contact','daily','hourly','initials')

    def profile(self):
        stude = Profile(
            firstname = self.validated_data['firstname'],
            lastname = self.validated_data['lastname'],
            contact = self.validated_data['contact'],
            daily = self.validated_data['daily'],
            hourly = self.validated_data['hourly'],
            initials = self.validated_data['initials'],
        )
        stude.save()
        return stude

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('firstname', 'lastname','contact','hourly','daily','initials')
