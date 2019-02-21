from rest_framework.generics import (ListAPIView, RetrieveAPIView)
from items.models import Item, FavoriteItem
from rest_framework.filters import (OrderingFilter, SearchFilter)
from rest_framework.permissions import (AllowAny,) 
from .serializers import ItemListSerializer, ItemDetailSerializer
from .permissions import IsAdder
# Create you here.
class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = [AllowAny,]
    filter_backends = [OrderingFilter, SearchFilter,]
    search_fields = ['name', 'description']

class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    permission_classes = [IsAdder, ]
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'