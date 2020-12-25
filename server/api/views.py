from datetime import datetime

from django.db import connections
from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from server.api.models import AuthUser, Category, Product, DangerLevel
from server.api.serializers import UserSerializer, CategorySerializer, ProductSerializer, DangerLevelSerializer


class AuthTokenLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        user.last_login = datetime.now()
        user.save()

        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                'token': token.key,
                'user': UserSerializer(user).data,
            },
            status=status.HTTP_200_OK
        )


class Me(APIView):
    serializer = UserSerializer
    model = AuthUser
    http_method_names = ['get', 'patch']
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        # me = self.model.objects.get(id=request.user.id)
        me = AuthUser.objects.raw('''SELECT * FROM auth_user WHERE id = %s ORDER BY id''', [request.user.id])[0]
        serializer = self.serializer(me)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        user = self.model.objects.get(id=request.user.id)
        serializer = self.serializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCategory(APIView):
    serializer = CategorySerializer
    model = Category
    http_method_names = ['get', 'post']
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        # categories = self.model.objects.all()
        categories = list(Category.objects.raw('''SELECT * FROM category ORDER BY id'''))
        serializer = self.serializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        cursor = connections['default'].cursor()
        cursor.execute(
            '''INSERT INTO "category" (name, description) VALUES (%s, %s)''',
            [request.data.get('name'), request.data.get('description')]
        )

        categories = list(Category.objects.raw('''SELECT * FROM category ORDER BY id'''))
        serializer = self.serializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ListDangerLevels(APIView):
    serializer = DangerLevelSerializer
    model = DangerLevel
    http_method_names = ['get', 'post']
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        danger_levels = self.model.objects.all()
        serializer = self.serializer(danger_levels, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        cursor = connections['default'].cursor()
        cursor.execute(
            '''INSERT INTO "danger_level" (name, color) VALUES (%s, %s)''',
            [request.data.get('name'), request.data.get('color')]
        )

        levels = list(DangerLevel.objects.raw('''SELECT * FROM danger_level ORDER BY id'''))
        serializer = self.serializer(levels, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ListProduct(APIView):
    serializer = ProductSerializer
    model = Product
    http_method_names = ['get', 'post']
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        # products = self.model.objects.all()
        products = list(Product.objects.raw('''SELECT * FROM product ORDER BY id'''))
        serializer = self.serializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        cursor = connections['default'].cursor()
        cursor.execute('''
            INSERT INTO "product" (name, description, price, is_impact_on_environment, is_available, danger_level_id, category_id, picture)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', [
            data.get('name'),
            data.get('description'),
            data.get('price'),
            data.get('isImpact'),
            data.get('isAvailable'),
            data.get('level'),
            data.get('category'),
            data.get('picture')
        ])

        products = list(Product.objects.raw('''SELECT * FROM product ORDER BY id'''))
        serializer = self.serializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)