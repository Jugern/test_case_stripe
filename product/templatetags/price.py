from django import template
from decimal import Decimal
from product.models import Order

register = template.Library()

@register.filter
def add_price(context):
        return context
