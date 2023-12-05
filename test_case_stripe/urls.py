"""
URL configuration for test_case_stripe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product.views import (AddItem,
                           BuyTovar,
                           BuyList,
                           CancelView,
                           DelItem,
                           ItemsAll,
                           ItemTitle,
                           MainMenu,
                           OrderBuy,
                           PriceOnline,
                           SuccessView,
                           )

urlpatterns = [
    path('', MainMenu.as_view(), name='main'),
    path('AddItem/<pk>', AddItem.as_view(), name='AddItem'),
    path('DelItem/<pk>', DelItem.as_view(), name='DelItem'),
    path('buy/<pk>', BuyTovar.as_view(), name='buy'),
    path('buylist/<uuid:id>', BuyList.as_view(), name='buylist'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('items/', ItemsAll.as_view(), name='items'),
    path('item/<pk>', ItemTitle.as_view(), name='item-pk'),
    path('order/', OrderBuy.as_view(), name='order-buy'),
    # path('create_check/<pk>', CreateCheckoutSessionView.as_view(), name='create_check'),
    path('success/', SuccessView.as_view(), name='success'),
    path('admin/', admin.site.urls),
    path('api/v1/price/', PriceOnline.as_view(), name='api-price'),
]
