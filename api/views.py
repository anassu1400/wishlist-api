from rest_framework.generics import (ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView,)
from items.models import Item, FavoriteItem
from rest_framework.filters import (OrderingFilter, SearchFilter)
from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser) 
from .serializers import ItemListSerializer, ItemDetailSerializer

# Create you here.
class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	permission_classes = [IsAuthenticated,]
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['name', 'description']

class ItemDetailView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	permission_classes = [IsAuthenticated,]
