from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class FavoritedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = FavoriteItem
        fields = ['user']
    

class ItemListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
    added_by = UserSerializer()
    user_count = serializers.SerializerMethodField()
    
    class Meta:
        model= Item
        fields = ['name', 'description', 'detail', 'added_by', 'user_count']
    def get_user_count(self, obj):
        return obj.favorited.count()
    

class ItemDetailSerializer(serializers.ModelSerializer):
    favorited = FavoritedSerializer(many=True)
    added_by = UserSerializer()
    class Meta:
        model= Item
        fields = ['name', 'description', 'added_by','favorited']