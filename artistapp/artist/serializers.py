from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ContentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Content
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name','last_name','age','birth_date','city','phone',]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email','password','profile']

    def create(self, validated_data):
        password = self.validated_data.get('password')
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user, **profile_data)
        return user
