from rest_framework import serializers

from server.api.models import AuthUser, Category, Product


class UserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name', required=True)
    lastName = serializers.CharField(source='last_name', required=True)
    password = serializers.CharField(write_only=True, required=True)
    dateJoined = serializers.DateTimeField(source='date_joined', required=False)
    role = serializers.SerializerMethodField()

    def get_role(self, obj):
        return obj.role.name

    class Meta:
        model = AuthUser
        fields = [
            'username',
            'firstName',
            'lastName',
            'password',
            'email',
            'phone',
            'dateJoined',
            'address',
            'role',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
