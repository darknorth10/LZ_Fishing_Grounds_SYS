from django.shortcuts import render, redirect
from Products.models import Products
from django.contrib import messages
from . models import Cart, Item, Transaction
from django.db.models import Sum, Q
import locale
from decimal import Decimal
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    
    page_name = "pos"
    products = Products.objects.all()
    
    if request.GET.get("search"):
        search = request.GET.get("search")
        products = Products.objects.filter(Q(name__icontains=search) | Q(category__icontains=search))

    
    cart = Cart.objects.all().order_by('-id')
    cart_size = len(cart)
    
    # adding items to cart
    if request.method == "POST":
        prod_id = request.POST.get("id")
        quantity = request.POST.get("quantity")
        quantity = int(quantity)
        
        if prod_id and quantity > 0:
            product = Products.objects.get(id=int(prod_id))
            
            _cart = Cart.objects.filter(product_id = prod_id).first()
            
            # checks if the item is alreaddy at the cart if yes, update the item info but if not just create it
            if _cart is None:
                if product.stocks >= quantity:
                    subtotal_item = product.price * quantity
                    
                    new_cart = Cart(product_id=int(prod_id), product_name=product.name, quantity=quantity, subtotal=subtotal_item)
                    new_cart.save()
                else:
                    messages.add_message(request, messages.ERROR, "Desired quantity exceeded current stocks.")
                    print("Desired quantity exceeded current stocks")
            else:
                if product.stocks >= _cart.quantity + quantity:
                    _cart.quantity += quantity
                    _cart.subtotal += product.price * quantity
                    _cart.save()
                else:
                    messages.add_message(request, messages.ERROR, "Desired quantity exceeded current stocks.")
                    print("Desired quantity exceeded current stocks")
        
        else:
            messages.add_message(request, messages.ERROR, "Invalid Request.")
            print("Invalid Request")
        
    
    cart_subtotal = Cart.objects.aggregate(Sum('subtotal'))
        
    if cart_subtotal['subtotal__sum'] is not None:
        
        cart_subtotal = "{:,}".format(cart_subtotal['subtotal__sum'])
        # cart_subtotal = cart_subtotal['subtotal__sum']
    else:
        cart_subtotal = "0.00"
    context = {
        'page_name': page_name,
        'products': products,
        'cart': cart,
        'cart_size': cart_size,
        'cart_subtotal': cart_subtotal,
    }
    
    return render(request, "./pos/index.html", context)



def delete_item(request, id):
    
    item = Cart.objects.get(pk=id)
    print(item)
    if item is None:
        messages.add_message(request, messages.ERROR, "Error removing item from the cart.")
    else:
        item.delete()
        messages.add_message(request, messages.SUCCESS, "Item has been removed from the cart.")
        
        
    return redirect("pos")


def transaction_view(request):
    cart = Cart.objects.all()
    
    if request.method == "POST":
        
        if request.POST.get('payment'):
            cart_subtotal = Cart.objects.aggregate(Sum('subtotal'))['subtotal__sum']
            change = 0
            payment = Decimal(request.POST.get('payment'))
            payment_type = request.POST.get('payment_type')
            
            if payment >= cart_subtotal:
                 change = payment - cart_subtotal
                 new_transaction = Transaction(cashier=request.user.username, payment=payment, change=change, payment_method=payment_type, total=cart_subtotal)
                 
                 new_transaction.save()
                 
                 transaction = Transaction.objects.all().order_by('-id').first()
                 
                 for item in cart:
                     new_item = Item(tnum=transaction.id, quantity=item.quantity, subtotal=item.subtotal, product_id=item.product_id)
                     new_item.save()
                     
                     prod = Products.objects.get(id=item.product_id)
                     prod.stocks -= item.quantity
                     prod.save()
                     
                     item.delete()
                     
                 messages.add_message(request, messages.SUCCESS, "Sucessful Transaction")
                 return redirect('pos')
            else:
                messages.add_message(request, messages.ERROR, "Insufficient amount")
                return redirect('pos')
            
def trasactions(request):
        
    trasactions = Transaction.objects.all().order_by('-id')
    
    # if request.GET.get("search"):
    #     if request.GET.get("search") is not None:
          
    #         search = request.GET.get("search")
    #         products = Products.objects.filter(Q(name__icontains=search) | Q(category__icontains=search) | Q(sub_category__icontains=search)).order_by('-id')
    page = "pos"
    
    # pagination
    paginator = Paginator(trasactions, 5) # shows 4 users per page
    
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    
    # variables rendered to the template
    context = {
        'page_name': page,
        'page_obj': page_obj,
        'page_char' : 'a' * page_obj.paginator.num_pages
    }
    
    return render(request, "pos/transactions.html", context)