from django.contrib.auth.models import Group
from rest_framework import routers, serializers, viewsets, generics
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        username = User.objects.create_user(validated_data['username'],
                                            email=validated_data['email'],
                                            password=validated_data['password'])

        return username


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        email = serializers.CharField(max_length=255)
        password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(requests=self.context.get('request'),
                                username=email, password=password)

            if not user:
                msg = "Невозможно войти в систему с предоставленными учетными данными."
                raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = "Должен включать в себя имя и пароль."
                raise serializers.ValidationError(msg, code='authorization')

            data['user'] = user
            return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
