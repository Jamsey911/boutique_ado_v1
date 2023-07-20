from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NUofrKWxlYc6JNxhTN88pa18iZgjK7OOg06Ev3yCjiRjTeF6xnd2Wy9CkfE9zo4d4co6gI2NR6MOBgf0noOlJKl00oicn7DWR',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
