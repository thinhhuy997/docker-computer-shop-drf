from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Category, Product, ImageURL, Note


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name", "product_list"]
        depth = 1


class ImageURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageURL
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    image_urls = serializers.SlugRelatedField(many=True,
                                              read_only=True,
                                              slug_field='url')

    class Meta:
        model = Product
        fields = ['id', 'slug', 'categories', 'image_urls', 'name',
                  'price', 'description_from_crawler', 'created_at', 'updated_at']
        depth = 1

# JWT TOKEN CUSTOMIZATION


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['user_id'] = user.id
        token['username'] = user.username
        token['email'] = user.email

        return token

# Test jwt-authen-authorization


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
