from django.urls import path

from src.goods.views import GoodsListView

urlpatterns = [
    path("goods/", GoodsListView.as_view()),
]