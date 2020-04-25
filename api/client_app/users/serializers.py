from rest_framework import serializers

from .models import UserProfile

class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    class Meta:
        model = UserProfile
        fields = ('id', 'email','name','password')
        extra_kwargs = {
            'password': {'write_only': True}
        }