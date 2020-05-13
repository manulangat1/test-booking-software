from .models import User,Test,Disease
from rest_framework import serializers
from django.contrib.auth import authenticate

# class UserSerializer(serializers.ModelSerializer):
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password =  serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        return serializers.ValidationError("Incorect Credential")
        # return super().validate(attrs)

# register serializers
class RegisterSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password'
        )
        extra_kwargs={'password':{'write_only':True}}
    def create(self, validated_data):
        # return super().create(validated_data)
        user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
        return user
# user serializer
class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'tel_no'
        )
class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self,value):
        return value
class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = (
            "id",
            "name",
            "test_for",
            "costs"
        )      
class TestSerializer(serializers.ModelSerializer):
    disease = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    class Meta:
        model = Test
        fields = (
            "id",
            "patient",
            "disease",
            "request_at",
            "total"
        )
    def get_disease(self,obj):
        print(obj.disease)
        return DiseaseSerializer(obj.disease.all(),many=True).data
    def get_total(self,obj):
        return obj.total()
