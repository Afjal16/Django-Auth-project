from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .forms import Registration,Edit_Registration
from django.contrib.auth.views import PasswordChangeForm,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


# Create your views here.
def auth_index(request):
    return render(request, 'auth_index.html')

def Login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        user=authenticate(username=username, password=password1)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request, 'Try Again')
            return redirect('/login')
        
    return render(request, 'login.html')

def registration(request):
    if request.method == 'POST':  
        form = Registration(request.POST)  
        if form.is_valid():  
            form.save() 
            username=form.cleaned_data['username'] 
            password=form.cleaned_data['password1'] 
            user=authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, 'Account created successfully') 
            return redirect('/login') 
  
    else:  
        form = Registration()  
    context = {  
        'form':form  
    }  
  
    
    
    
    
    
    # if request.method=="POST":
    #     username=request.POST.get('username')
    #     email=request.POST.get('email')
    #     password1=request.POST.get('password1')
    #     password2=request.POST.get('password2')
        
    #     if password1!=password2:
    #         messages.success(request,'Password is not Matching')
    #         return redirect('/registration')
        
    #     user=User.objects.create_user(username,email,password1)
    #     user.save()
    #     messages.success(request,"User is Created Please Login")
    #     return redirect('/login')
        
    return render(request, 'registration.html',context)


def edit_registration(request):
    if request.method == 'POST':  
        form = Edit_Registration(request.POST, instance=request.user)  
        if form.is_valid():  
            form.save() 
            messages.success(request, 'Account Updated successfully') 
            return redirect('/') 
  
    else:  
        form = Edit_Registration(instance=request.user)  
    context = {  
        'form':form  
    } 
    return render(request, 'edit_registration.html',context)


def change_password(request):
    if request.method == 'POST':  
        form = PasswordChangeForm(data=request.POST, user=request.user)  
        if form.is_valid():  
            form.save() 
            update_session_auth_hash(request,form.user)
            messages.success(request, 'Change Password successfully') 
            return redirect('/') 
  
    else:  
        form = PasswordChangeForm(user=request.user)  
    context = {  
        'form':form  
    } 
    return render(request, 'change_password.html',context)



class ResetPassword(PasswordResetView):
    template_name='ResetPassword.html'
    
    
class ResetPassword_Done(PasswordResetDoneView):
    template_name='ResetPassword_Done.html'
    
    
class ResetPassword_Confirm(PasswordResetConfirmView):
    template_name='ResetPassword_Confirm.html'
    
    
class ResetPassword_Complete(PasswordResetCompleteView):
    template_name='ResetPassword_Complete.html'




def Logout(request):
    logout(request)
    messages.success(request,"Logout Successful")    
    return redirect('/login')