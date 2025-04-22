from rest_framework import serializers
from schApp.models import CustomUser, School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"
        extra_kwargs = {"created_on": {"read_only": True}}


class CustomUserSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(queryset = School.objects.all())
    class Meta:
        model = CustomUser
        fields = ["id", "username", "password", "email", "school", "role"]
        extra_kwargs = {"password": {"write_only": True}, "email": {"required": True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
