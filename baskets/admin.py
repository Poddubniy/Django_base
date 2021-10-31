from django.contrib import admin
from baskets.models import Basket


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')  # помещая в один кортеж, поля размещаются на одной линии
    extra = 0  # убираем лишнии поля
