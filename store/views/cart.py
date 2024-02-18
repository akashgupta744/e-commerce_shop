from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        # print(products)
        tax_rate = 2 / 100
        # for p in products:
        #     print(p)
        #     print(p.price)
        taxs = {product.id: product.price * tax_rate for product in products}
        # print(taxs)
        total_with_tax = sum(product.price*(1+(tax_rate)) for product in products)


        return render(request, 'cart.html', {'products': products, 'taxs': taxs, 'total_with_tax': total_with_tax})