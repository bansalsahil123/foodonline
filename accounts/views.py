from django.shortcuts import render, redirect
from .forms import UserForm
from vendor.forms import VendorForm
from .models import User
from django.contrib import messages
# Create your views here.

def register_user(request):
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            password = forms.cleaned_data["password"]
            user = forms.save(commit=False)
            user.role = User.CUSTOMER
            user.set_password(password)
            user.save()
            messages.success(request,"Register Successfully!!")
            return redirect('register_user')
        else:
            print(forms)         
            
    else:
        forms = UserForm()
    context = {"forms":forms}
    return render(request,'accounts/registerUser.html',context=context)



def register_vendor(request):
    if request.method == "POST":
        forms = UserForm(request.POST)
        v_form = VendorForm(request.POST)
        if forms.is_valid():
            user = forms.save(commit=False)
            user.role = User.RESTURANT
            user.save()
            vendor = v_form.save(commit=False)
            

    else:
        forms = UserForm()
        v_form = VendorForm()
    context = {"forms":forms,"v_form":v_form}
    return render(request,'accounts/registerVendor.html',context=context)