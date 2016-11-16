from rest_framework import serializers
from backend.apps.pro.models import Pro
from backend.authentification.models import User
from backend.libs.media import Base64ImageField

class ProSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Pro
        fields = ('__all__')

class SignUpProSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    pro = serializers.SerializerMethodField(read_only=True)

    def get_token(self, obj):
        return obj.user_set.all()[0].token()

    def get_pro(self, obj):
        return ProSerializer(obj).data

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Cet email existe déjà.')
        return value

    def create(self, validated_data):
        return Pro.signup(**validated_data)

    class Meta:
        model = Pro
        fields = ('company', 'phone', 'email', 'password', 'first_name', 'last_name', 'token', 'pro')
        extra_kwargs = {
            'company': {'required': True, 'write_only' : True},
            'email': {'required': True},
            'password': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone': {'required': True, 'write_only' : True},
        }


