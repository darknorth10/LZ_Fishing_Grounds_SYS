from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductCreationForm
from .models import Products
from django.core.paginator import Paginator

# Main Page of Products in admin side
def index(request):
    
    products = Products.objects.all(),
    page_name = "products"
    product_form = ProductCreationForm()
        # pagination
    paginator = Paginator(products, 5) # shows 4 users per page
    
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    context = {
        'products' : Products.objects.all(),
        'page_name': page_name,
        'form': product_form
    }
    
    return render(request, "products/index.html", context)

# add product page
def create_product_page(request):
    
    form = ProductCreationForm()
    
    if request.method == "POST":
        form = ProductCreationForm(request.POST)
        
        if form.is_valid:
            form.save()
            return redirect('product_management')
    context = {
        'form': form
    }
    return render(request, "products/new_product.html", context)

# update product page
def update_product_page(request, id):
    
    obj = get_object_or_404(Products, id=id)
    
    form = ProductCreationForm(request.POST or None, request.FILES or None, instance = obj)
    
    
    if request.method == "POST":
        
        if form.is_valid:
            form.save()
            return redirect('product_management')
        else:
            print(form.errors)
            
    context = {
        'form': form
    }
    
    
    return render(request, "products/update_product.html", context)