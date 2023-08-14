from rest_framework import generics

from src.goods.models import Goods
from src.goods.serializers import GoodsSerializer


class GoodsListView(generics.ListAPIView):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()