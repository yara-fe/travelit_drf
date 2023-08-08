from rest_framework import serializers
from .models import CustomUser

#Convert Reward model to JSON
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}} #only write password, but do not return to user

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data) #password hashing