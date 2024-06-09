from django.shortcuts import render, redirect, get_object_or_404
from .models import CarModel
from login.forms import LoginUserForm
from .forms import CommentForm
from .models import CommentModel
from order_history.models import OrderModel, OrderItemModel
from brand.models import BrandModel

# Create your views here.
def home_page(request, brand_slug=None):
    brand_list = BrandModel.objects.all()

    if brand_slug:
        brand = get_object_or_404(BrandModel, slug=brand_slug)
        car_data = CarModel.objects.filter(brand=brand)
    else:
        car_data = CarModel.objects.all()

    return render(request, "home.html", {"brand_list": brand_list, "car_data": car_data})



def car_details_page(request, name):
    post = get_object_or_404(CarModel, slug=name)
    comments = CommentModel.objects.all()
    print(comments)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post 
            comment.save()
            return redirect("car_details", name)
    else: 
        form = CommentForm()
    return render(request, "car_details.html", {"data": post, "form": form, "comments": comments})

def add_to_cart(request, name):
    product = get_object_or_404(CarModel, slug=name)
    order, created = OrderModel.objects.get_or_create(user=request.user)
    
    if product.quantity > 0:
        order_item, created = OrderItemModel.objects.get_or_create(order=order, product=product)
        
        if not created:
            order_item.quantity += 1
        order_item.save()
        
        product.quantity -= 1
        product.save()
        
        return redirect("user_profile")
    else:
        return redirect("home")    
