from django.contrib import admin
from baskets.models import Basket


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')  # помещая в один кортеж, поля размещаются на одной линии
    readonly_fields = ('created_timestamp',)
    extra = 0  # убираем лишнии поля
