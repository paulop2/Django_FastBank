from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.translation import gettext as _

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'frist_name', 'last_mame', 'cpf']
        extra_kwargs = {
            'password': {'write_only': True, 'min_lenght': 8},
            'is_active': {'read_only': True},
            'created_at': {'read_only': True},

        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
