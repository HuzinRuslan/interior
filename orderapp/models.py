from django.conf import settings
from django.db import models

from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'
    DONE = 'DN'

    ORDER_STATUSES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен в обработку'),
        (PROCEEDED, 'обработан'),
        (PAID, 'оплачен'),
        (READY, 'готов к выдаче'),
        (DONE, 'выдан'),
        (CANCEL, 'отменен'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    status = models.CharField(max_length=3, choices=ORDER_STATUSES, default=FORMING)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Текущий заказ: #{self.id}'

    # def get_total_quantity(self):
    #     items = self.orderitems.select_related()
    #     return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_quantity(self):
        items = self.orderitems.select_related()
        return len(items)

    # def get_total_cost(self):
    #     items = self.orderitems.select_related()
    #     return sum(list(map(lambda x: x.quantity * x.product.price, items)))

    def get_summary(self):
        items = self.orderitems.select_related()
        total_cost = sum(list(map(lambda x: x.quantity * x.product.price, items)))
        total_quantity = sum(list(map(lambda x: x.quantity, items)))

        return {
            'total_cost': total_cost,
            'total_quantity': total_quantity
        }

    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()

        self.is_active = False
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')

    def get_product_cost(self):
        return self.product.price * self.quantity

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.get(pk=pk)
