from django.shortcuts import render, get_object_or_404, redirect

from .models import Products
from .forms import ProductModelForm, DjangoProductsForm
from django.http import Http404
from django.urls import reverse

# Create your views here.
def prodcuts_details_view(request, *args, **kargs):
    obj = Products.objects.get(id=1)
    context = {
        'objectItem': obj,
        'list': [1,2,3,4]
    }
    return render(request, "products/products_details.html", context)

def products_form_view(request):
    # FORMS INICIAL
    # form = ProductModelForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     form = ProductModelForm()
    
    # context = {
    #     'form': form
    # }


    # FORMS NO HTML
    # context = {}
    # if request.method == "POST":
    #     new_title = request.POST.get('title')
        
    #     new_description = request.POST.get('description')
        
    #     new_price = request.POST.get('price')
        
    #     Products.objects.create(title=new_title, description=new_description, price=new_price)


    # FORMS NO DJANGO
    # product_form = DjangoProductsForm()
    # if request.method == 'POST':
    #     product_form = DjangoProductsForm(request.POST)
    #     if product_form.is_valid():
    #         print(product_form.cleaned_data)
    #         Products.objects.create(**product_form.cleaned_data)
    #         product_form = DjangoProductsForm()
    #     else:
    #         print(product_form.errors)
    # context = {
    #     'form': product_form,
    # }

    # FORMS VALIDATION

    initial_data = {
        'title':'Title'
    }

    form = ProductModelForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductModelForm(initial=initial_data)
    
    context = {
        'form': form
    }

    # OU
    product_form = DjangoProductsForm(initial=initial_data)
    if request.method == 'POST':
        product_form = DjangoProductsForm(request.POST, initial=initial_data)
        if product_form.is_valid():
            print(product_form.cleaned_data)
            Products.objects.create(**product_form.cleaned_data)
            product_form = DjangoProductsForm(initial=initial_data)
        else:
            print(product_form.errors)
    context = {
        'form': product_form,
    }

    return render(request, "products/products_forms.html", context)

def dynamic_links(request, my_id):
    try:
        obj = Products.objects.get(title=my_id)
    except Products.DoesNotExist:
        raise Http404

    context = {
        'object':obj,
    }
    return render(request,'products/dynamic_products.html', context)

def products_delete_view(request,my_id):
    obj = get_object_or_404(Products, id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect ('../')
    
    context = {
        "object": obj
    }

    return render(request, "products/delete.html", context)

def product_lsit_view(request):
    queryset = Products.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)

# LINKS DINAMICOS
def product_create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductModelForm()
    
    context = {
        'form': form
    }
    
    return render(request, "products/products_create.html", context)
    
def product_update_view(request, id):
    obj = get_object_or_404(Products, id=id)
    form = ProductModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
        
    context = {
        'form': form
    }
    
    return render(request, "products/products_create.html", context)

def product_list_view(request):
    queryset = Products.objects.all()    
    context = {
        "object_list":queryset,
        "add_form_link": reverse('products:product-create')

    }
    
    return render(request, "products/products_list.html", context)

def product_detail_view(request, id):
    obj = get_object_or_404(Products, id=id)
        
    context = {
        'object': obj
    }
    
    return render(request, "products/products_details.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Products, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    
    return render(request, "products/products_delete.html", context)





