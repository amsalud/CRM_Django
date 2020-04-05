from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm, SignupForm
from .filters import OrderFilter

# Create your views here.

def signup(request):
    form  = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = { 'form': form}
    return render(request, 'accounts/signup.html', context)

def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()
    orders_out_for_delivery = orders.filter(status='Out for delivery').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending,
        'orders_out_for_delivery': orders_out_for_delivery
    }
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = customer.order_set.all()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': orders.count(),
        'myFilter': myFilter
    }
    return render(request, 'accounts/customer.html', context)

def createOrder(request, customer_id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=customer_id)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = { 'formset': formset }
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = { 'form': OrderForm(instance=order) }
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, id):
    order = Order.objects.get(id=id)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = { 'item': order }
    return render(request, 'accounts/delete.html', context)

def deleteCustomer(request, id):
    customer = Customer.objects.get(id=id)

    if request.method == 'POST':
        customer.delete()
        return redirect('/')

    context = { 'item': customer }
    return render(request, 'accounts/delete.html', context)