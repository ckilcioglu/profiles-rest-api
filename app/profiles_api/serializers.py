from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for our APIView"""

    name = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=100)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    
    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class PhoneBookSerializer(serializers.ModelSerializer):
    """Serializes a phone book contact"""
    
    class Meta:
        model = models.PhoneBook
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'phone_number']
    
    def validate_phone_number(self, value):
        if value[0] == "+":
            value = "00" + value[1:]
        if value.isnumeric():
            return value
        else:
            raise serializers.ValidationError("Wrong phone number format")