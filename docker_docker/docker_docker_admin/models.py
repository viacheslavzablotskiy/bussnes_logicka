from itertools import count

from django.db import models
from django.contrib.auth.models import User
from .services import discount
from django.db.models.signals import post_save
from django.dispatch import receiver


class CodeName(models.Model):
    code = models.CharField(max_length=255, null=True, unique=True)
    name = models.CharField(max_length=255, null=True, unique=True)

    def __str__(self):
        return f'{self.name}:{self.code}'


class Currency(models.Model):
    valuta = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return f'{self.valuta}'


class Item(models.Model):
    name = models.ForeignKey('CodeName', max_length=255, blank=True, null=True, on_delete=models.SET_NULL)
    valuta = models.ForeignKey('Currency', blank=True, null=True, on_delete=models.CASCADE)
    price = models.ForeignKey('Price', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'



class Price(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2, max_length=5, null=True, blank=True)
    # total_price = models.IntegerField(default=1)
    # total_price_item = models.DecimalField(max_digits=5, decimal_places=2, max_length=5, null=True, blank=True)

    def __str__(self):
        return f'{self.price}'

    # def save(self, *args, **kwargs):
    #     price_item = 4
    #     price_item_1 = 8
    #     if self.price >= 25.00:
    #         self.price -= price_item
    #     else:
    #         self.price -= price_item_1
    #
    #     price_item_item = self.price
    #     self.total_price_item = self.total_price * price_item_item
    #     super(Price, self).save(*args, **kwargs)


    # @receiver(post_save, sender=Price)
    # def price_price(sender, instance, *args, **kwargs):
    #     price_item = instance.price
    #     instance.price_item_price = instance.total_price * price_item
    #     instance.price_item_price.save()
    # def discount(self, discount: float = 3.00) -> str:
    #     if self.price > 25.00:
    #         return f'{self.price - discount}'

    # def discount(self, discount: float = 0.012) -> str:
    #     return f'{(float(self.price) / discount)}'


class WatchList(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey("Item", blank=True, null=True, on_delete=models.SET_NULL)
    is_publishid = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.item}'


class Offer(models.Model):
    RATE_CHOICES = (
        (1, 'BUY'),
        (2, 'ADD'),
    )
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.CASCADE)
    total_price_is_offer = models.DecimalField(max_digits=5, decimal_places=2, max_length=5, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    type_function = models.PositiveIntegerField(choices=RATE_CHOICES, null=True)

    def save(self, *args, **kwargs):
        price_item = self.item.price.price
        self.total_price_is_offer = self.quantity * price_item
        super(Offer, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.item}'


class Balans(models.Model):
    balans = models.DecimalField(max_digits=5, decimal_places=2, max_length=5, null=True, blank=True, default=400)

    def __str__(self):
        return f"{self.balans}"


class Trade(models.Model):
    client = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="client_trade",
                               related_query_name="client_trade")
    price_total = models.DecimalField(max_digits=5, decimal_places=2, max_length=5,null=True, blank=True)
    client_offer = models.ForeignKey('Offer', blank=True, null=True, on_delete=models.SET_NULL,
                                     related_name='client_offer_trade',
                                     related_query_name="client_offer_trade")
    balans_1 = models.ForeignKey(Balans, blank=True, null=True, on_delete=models.SET_NULL, related_name="balans_1",
                                 related_query_name="balans_1")
    ostatok_balanc = models.DecimalField(max_digits=5, decimal_places=2, max_length=5, null=True, blank=True)
    seller = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="seller_trade",
                               related_query_name="seller_trade")
    price_total_1 = models.DecimalField(max_digits=5, decimal_places=2, max_length=5, null=True, blank=True)
    seller_offer = models.ForeignKey('Offer', blank=True, null=True, on_delete=models.SET_NULL,
                                     related_name="seller_offer_trade",
                                     related_query_name="seller_offer_trade")
    balans_2 = models.ForeignKey(Balans, blank=True, null=True, on_delete=models.SET_NULL, related_name="balans_2",
                                 related_query_name="balans_2")
    ostatok_balanc_1 = models.DecimalField(max_digits=5, decimal_places=2, max_length=5, null=True, blank=True)

    def __str__(self):
        return f'{self.client_offer}'

    def save(self, *args, **kwargs):
        type_offer = self.client_offer.type_function
        type_offer_1 = self.seller_offer.type_function
        name_offer = self.client_offer.item.name
        name_offer_1 = self.seller_offer.item.name
        quantity_offer = self.client_offer.quantity
        quantity_offer_1 = self.seller_offer.quantity
        offer = self.client_offer
        offer_1 = self.seller_offer
        if (type_offer == 1 and type_offer_1 == 2) and name_offer == name_offer_1 \
                and quantity_offer == quantity_offer_1:
            total_price_is_item = self.client_offer.total_price_is_offer
            self.price_total = total_price_is_item
            total_price_is_item_1 = self.seller_offer.total_price_is_offer

            self.price_total_1 = total_price_is_item_1
            balans_sell = self.balans_1.balans
            balans_shell_2 = self.balans_2.balans
            self.ostatok_balanc = balans_sell - self.price_total
            self.ostatok_balanc_1 = balans_shell_2 + self.price_total_1
        elif (type_offer == 2 and type_offer_1 == 1) and name_offer == name_offer_1 \
                and quantity_offer == quantity_offer_1:
            total_price_is_item = self.client_offer.total_price_is_offer
            self.price_total = total_price_is_item
            total_price_is_item_1 = self.seller_offer.total_price_is_offer
            self.price_total_1 = total_price_is_item_1
            balans_sell = self.balans_1.balans
            balans_shell_2 = self.balans_2.balans
            self.ostatok_balanc = balans_sell + self.price_total
            self.ostatok_balanc_1 = balans_shell_2 - self.price_total_1
        super(Trade, self).save(*args, **kwargs)



    # def save(self, *args, **kwargs):
    #     type_offer = self.client_offer.type_function
    #     type_offer_1 = self.seller_offer.type_function
    #     if type_offer == 1 and type_offer_1 == 1:
    #         total_price_is_item = self.client_offer.total_price_is_offer
    #         self.price_total = total_price_is_item
    #         total_price_is_item_1 = self.seller_offer.total_price_is_offer
    #         self.price_total_1 = total_price_is_item_1
    #         balans_sell = self.balans_1.balans
    #         balans_shell_2 = self.balans_2.balans
    #         self.ostatok_balanc = balans_sell - self.price_total
    #         self.ostatok_balanc_1 = balans_shell_2 - self.price_total_1
    #     elif type_offer == 2 and type_offer_1 == 2:
    #         total_price_is_item = self.client_offer.total_price_is_offer
    #         self.price_total = total_price_is_item
    #         total_price_is_item_1 = self.seller_offer.total_price_is_offer
    #         self.price_total_1 = total_price_is_item_1
    #         balans_sell = self.balans_1.balans
    #         balans_shell_2 = self.balans_2.balans
    #         self.ostatok_balanc = balans_sell + self.price_total
    #         self.ostatok_balanc_1 = balans_shell_2 + self.price_total_1
    #     elif type_offer == 1 and type_offer_1 == 2:
    #         total_price_is_item = self.client_offer.total_price_is_offer
    #         self.price_total = total_price_is_item
    #         total_price_is_item_1 = self.seller_offer.total_price_is_offer
    #         self.price_total_1 = total_price_is_item_1
    #         balans_sell = self.balans_1.balans
    #         balans_shell_2 = self.balans_2.balans
    #         self.ostatok_balanc = balans_sell - self.price_total
    #         self.ostatok_balanc_1 = balans_shell_2 + self.price_total_1
    #     elif type_offer == 2 and type_offer_1 == 1:
    #         total_price_is_item = self.client_offer.total_price_is_offer
    #         self.price_total = total_price_is_item
    #         total_price_is_item_1 = self.seller_offer.total_price_is_offer
    #         self.price_total_1 = total_price_is_item_1
    #         balans_sell = self.balans_1.balans
    #         balans_shell_2 = self.balans_2.balans
    #         self.ostatok_balanc = balans_sell + self.price_total
    #         self.ostatok_balanc_1 = balans_shell_2 - self.price_total_1
    #     super(Trade, self).save(*args, **kwargs)


class Inventory(models.Model):
    name_item = models.CharField(max_length=255, null=True, blank=True)
    item_1 = models.ForeignKey('Item', blank=True, null=True, on_delete=models.CASCADE, related_name="item_name_2",
                               related_query_name="item_name_2")
    count_item = models.ForeignKey('Item', blank=True, null=True, on_delete=models.CASCADE, related_name="item_name_3",
                             related_query_name="item_name_3")
    quantity = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.name_item}'

    # def count(self, *args, **kwargs):
    #     super(Inventory, self).save(*args, **kwargs)
    #
    def save(self, *args, **kwargs):
        name_item = Item.objects.all().count()
        self.quantity = name_item
        super(Inventory, self).save(*args, **kwargs)
