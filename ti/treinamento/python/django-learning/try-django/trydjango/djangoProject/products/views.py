from django.shortcuts import render

from .models import Products
from .forms import ProductModelForm, DjangoProductsForm

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
    product_form = DjangoProductsForm()
    if request.method == 'POST':
        product_form = DjangoProductsForm(request.POST)
        if product_form.is_valid():
            print(product_form.cleaned_data)
            Products.objects.create(**product_form.cleaned_data)
            product_form = DjangoProductsForm()
        else:
            print(product_form.errors)
    context = {
        'form': product_form,
    }

    return render(request, "products/products_forms.html", context)