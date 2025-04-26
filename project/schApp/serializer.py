from rest_framework import serializers
from schApp.models import CustomUser, School
import uuid

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},  # Ensure ID is read-only
            "created_on": {"read_only": True}
        }

    def create(self, validated_data):
        # Generate UUID if not provided
        if 'id' not in validated_data:
            validated_data['id'] = uuid.uuid4()
        return super().create(validated_data)

class CustomUserSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(),
        pk_field=serializers.UUIDField()  # Specify UUID field for relation
    )
    
    class Meta:
        model = CustomUser
        fields = ["id", "username", "password", "email", "school", "role"]
        extra_kwargs = {
            "id": {"read_only": True},  # Ensure ID is read-only
            "password": {"write_only": True},
            "email": {"required": True}
        }

    def create(self, validated_data):
        # Generate UUID if not provided
        if 'id' not in validated_data:
            validated_data['id'] = uuid.uuid4()
        return CustomUser.objects.create_user(**validated_data)