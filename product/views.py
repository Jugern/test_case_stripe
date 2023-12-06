import uuid

import stripe
from decimal import Decimal
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from .models import Item, Order


stripe.api_key = settings.STRIPE_SECRET_KEY


class MainMenu(TemplateView):
    template_name = 'index.html'


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class ItemsAll(TemplateView):
    template_name = 'items.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context


class ItemTitle(TemplateView):
    template_name = 'item-price.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get(id=self.kwargs["pk"])
        context = super().get_context_data(**kwargs)
        context.update({
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLISHABLE_KEY,
            'item': item,
            'url': reverse('buy', kwargs={'pk': self.kwargs["pk"]}),
        })
        return context


class BuyTovar(View):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs["pk"])
        domain = settings.ALLOWED_HOSTS[0]
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(item.price * 100),
                        'product_data': {
                            'name': item.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })
#         # return redirect(checkout_session.url)



class BuyList(View):

    def get(self, request, *args, **kwargs):
        client = Order.objects.get(user_id=self.kwargs["id"])
        allItem = [{
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(i.price * 100),
                'product_data': {
                    'name': i.name,
                },
            },
            'quantity': 1,
        } for i in client.item_list.all()]

        domain = settings.ALLOWED_HOSTS[0]
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"

        charge = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=allItem,
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )

        return JsonResponse({
            'id': charge.id
        })


class AddItem(TemplateView):

    def get(self, request, *args, **kwargs):
        item = Item.objects.get(id=kwargs['pk'])
        user_id = request.COOKIES.get('user_id')
        try:
            client = Order.objects.get(user_id=user_id)
            if client.item_list.filter(id=kwargs['pk']).exists():
                return JsonResponse({
                    'otvet': 'Товар уже есть в корзине',
                })
            else:
                client.total_amount += item.price
                client.item_list.add(item)
                client.save()
                return JsonResponse({
                    'otvet': 'Товар добавлен в корзину',
                })
        except:
            pass

        return JsonResponse({
            'yes': 'yes',
        })


class DelItem(TemplateView):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(id=kwargs['pk'])
        user_id = request.COOKIES.get('user_id')
        try:
            client = Order.objects.get(user_id=user_id)
            if client.item_list.filter(id=kwargs['pk']).exists():
                client.total_amount -= item.price
                client.item_list.remove(item)
                client.save()
                return JsonResponse({
                    'otvet': 'Товар удален из корзины',
                })
            else:
                return JsonResponse({
                    'otvet': 'Товара нет в корзине',
                })
        except:
            pass

        return JsonResponse({
            'yes': 'yes',
        })


class PriceOnline(TemplateView):

    def get(self, request, *args, **kwargs):
        user_price = Decimal(str(0.00))
        user_id = request.COOKIES.get('user_id')
        try:
            client = Order.objects.get(user_id=user_id)
            user_price = client.total_amount
            return JsonResponse({
                'price': user_price
            })
        except:
            client = Order(
                order_number='Идентификатор',
                total_amount=Decimal(str(0.00)),
                user_id=user_id,
            )
            client.save()
            return JsonResponse({
                'price': user_price
            })

class OrderBuy(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.COOKIES.get('user_id')
        client = get_object_or_404(Order, user_id=user_id)
        items = client.item_list.all()
        context.update({
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLISHABLE_KEY,
            'items': items,
            'url': f'../buylist/{user_id}',
        })
        return context



