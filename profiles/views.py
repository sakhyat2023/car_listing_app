from django.shortcuts import render, redirect
from order_history.models import OrderModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UpdateUserForm, ChangeUserPasswordForm

# Create your views here.
@login_required
def user_profile_page(request):
    cart, created = OrderModel.objects.get_or_create(user=request.user)
    orders = cart.items.select_related("product")
    
    return render(request, "user_profile.html", {"orders": orders, "user": request.user})

@login_required
def update_profile(request):
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Update successfully")
            return redirect("user_profile")
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, "update_profile.html", {"form": form})

@login_required
def change_password(request):
    if request.method == "POST":
        form = ChangeUserPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,"Password update successfully")
            return redirect("user_profile")
    else:
        form = ChangeUserPasswordForm(request.user)
    return render(request, "change_password.html", {"form": form})

    
    
    
    
