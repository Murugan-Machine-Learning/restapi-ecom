from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type', 'gender', 'first_name', 'last_name', 'country', 'city', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            user_type=validated_data['user_type'],
            gender=validated_data['gender'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            country=validated_data['country'],
            city=validated_data['city'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
