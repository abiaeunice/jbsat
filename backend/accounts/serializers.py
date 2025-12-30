from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'role', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Decode the access token and add custom claims
        access_token = self.get_token(self.user).access_token
        access_token["role"] = self.user.role
        access_token["email"] = self.user.email

        data["access"] = str(access_token)

        return data