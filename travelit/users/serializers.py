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
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

    # Define delete method
    def delete(self, instance):
        instance.delete()