import decimal
from uuid import uuid4
from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField('Имя товара', max_length=128)
    description = models.TextField('Описание товара', max_length=1000)
    price = models.DecimalField('Цена товара', max_digits=11, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    item_list = models.ManyToManyField(Item, related_name='items', verbose_name='Заказ', default=[], blank=True,)
    order_number = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=11, decimal_places=2, default=decimal.Decimal(str(0.00)))
    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    def __str__(self):
        return self.order_number