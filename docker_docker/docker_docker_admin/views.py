from rest_framework import generics, mixins, viewsets
from .serializers import *
from docker_docker_admin.models import CodeName


class ItemViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = CodeName.objects.all()
    serializer_class = CodeNameSerializer


class Curenccy(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurenccySerializer


class Item_table(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class Price_price(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class WathList_table(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerialisers


class Offer_offer(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerialisers


class Trade_trade(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerialisers


class Inventory_inventory(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerialisers


class Balans_balans(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Balans.objects.all()
    serializer_class = BalansSerializers
