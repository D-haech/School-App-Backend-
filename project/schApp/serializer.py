from rest_framework import serializers
from schApp.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs= {
            "password":{'write_only':True}
        }

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)