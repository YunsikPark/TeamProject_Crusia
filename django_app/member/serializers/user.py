from rest_framework import serializers

from ..models import MyUser

__all__ = [
    'UserSerializer',
    'UserUpdateSerializer',
    'UserCreateSerializer',
]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'pk',
            'username',
            'email',
            'img_profile',
            'first_name',
            'last_name',
            'gender',
            'phone_num',
            'birthday',
            'preference_language',
            'preference_currency',
            'living_site',
            'introduce',
            'last_login',
            'date_joined',
        ]
        read_only_fields = [
            'pk',
            'username',
            'email',
            'last_login',
            'date_joined',
        ]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            'pk',
            'username',
            'password1',
            'password2',
            'img_profile',
        )
        read_only_fields = (
            'username',
            'email',
        )


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_email(self, email):
        if MyUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('This Email already exist')
        return email

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords didn\'t match')
        return data

    def save(self, *args, **kwargs):
        email = self.validated_data.get('email', '')
        password = self.validated_data.get('password1', '')
        user = MyUser.objects.create_user(
            email=email,
            password=password,
        )
        return user
