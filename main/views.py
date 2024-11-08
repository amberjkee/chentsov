from django.shortcuts import render
from .models import *
from .forms import *

def index(request):
    list = _get_list_of_parametrs()
    context = {
        'list':list,
        }
    return render(request, "main/index.html", context=context)

def order(request, num=0):
    list = Orders.objects.filter(term_num=num)
    context = {
        'list':list,
        }
    return render(request, "main/order.html", context=context)

def new_order(request):
    if request.method == 'POST':
        form = AddOrder(request.POST)
        try:
            form.save()
            return index(request)
        except:
            form.add_error(None, "Error")
    else:
        form = AddOrder()
    return render(request, "main/new_order.html",{"form": form,})

def new_customer(request):
    if request.method == 'POST':
        form = AddCustomer(request.POST)
        try:
            form.save()
            return index(request)
        except:
            form.add_error(None, "Error")
    else:
        form = AddCustomer()
    return render(request, "main/new_customer.html",{"form": form,})

def _get_list_of_parametrs():
    p = Products.objects.values()
    res = list(p)
    for t in res:      
        t['reserved_count'] = _get_reserved_count_by_type(t['id'])
        t['customers'] = _get_customers_by_type(t['id'])

    return res


def _get_reserved_count_by_type(t):
    c = 0
    for e in Products.objects.get(id = t).orders_set.all():
        c += e.count
    return c

def _get_customers_by_type(t):
    l=[]
    for e in Orders.objects.filter(type = t):
        if not (e.term_num) in l: l.append(e.term_num)
    return l

