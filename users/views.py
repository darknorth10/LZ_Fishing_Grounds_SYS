from django.shortcuts import redirect, render

from .models import CustomUser
from .forms import CustomUserCreationForm, SignInForm
from django.contrib.auth import authenticate, login, logout


# sign in view
def index(request):
    signInForm = SignInForm()
    signUpForm = CustomUserCreationForm()
    message = ""
    
    if request.method == "POST":
            signInForm = SignInForm(request.POST)
            
            # if valid
            if signInForm.is_valid():
                user = authenticate(
                    username = signInForm.cleaned_data['username'],
                    password = signInForm.cleaned_data['password'],
                )
                
                # if credentials are valid
                if user is not None:
                    login(request, user)
                    
                    if user.role == "customer":
                        return redirect('index')
                    elif user.role == "admin" or user.role == "staff":
                        return redirect('dashboard')
                    
                else:
                    print("Error")
                    message = "Incorrect username or password."
                    
                    
            else:
                signInForm = SignInForm()
                message = "Invalid values"
                
                       
    
    
    return render(request, 'index.html', context={'form' : signInForm, 'err': message, 'form2' : signUpForm})



#logout
def logout_view(request):
    
    logout(request)
    return redirect('index')


# For user registration / sign up
def sign_up(request):
    
    # render user creation form on the template
    signUpForm = CustomUserCreationForm()
    
    # give password field design bypass
    signUpForm.fields['password1'].widget.attrs.update({
        'class': "w-full h-full px-3 py-3 font-sans text-sm font-normal transition-all bg-transparent border rounded-md peer border-blue-gray-200 border-t-transparent text-blue-gray-700 outline outline-0 placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-gray-900 focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50",
        'placeholder': " ",
        'minlength' : "8"
    })
    signUpForm.fields['password2'].widget.attrs.update({
        'class': "w-full h-full px-3 py-3 font-sans text-sm font-normal transition-all bg-transparent border rounded-md peer border-blue-gray-200 border-t-transparent text-blue-gray-700 outline outline-0 placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-gray-900 focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50",
        'placeholder': " ",
        'minlength' : "8"
    })
    
    # if the user creation form has been sent
    if request.method == "POST":
        signUpForm = CustomUserCreationForm(request.POST)
        
        if signUpForm.is_valid():
            signUpForm.save()
            return redirect('email_sent')
            
        else:
            
            print(signUpForm.errors)
            signUpForm.fields['password1'].widget.attrs.update({
                'class': "w-full h-full px-3 py-3 font-sans text-sm font-normal transition-all bg-transparent border rounded-md peer border-blue-gray-200 border-t-transparent text-blue-gray-700 outline outline-0 placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-gray-900 focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50",
                'placeholder': " ",
                'minlength' : "8"
            })
            signUpForm.fields['password2'].widget.attrs.update({
                'class': "w-full h-full px-3 py-3 font-sans text-sm font-normal transition-all bg-transparent border rounded-md peer border-blue-gray-200 border-t-transparent text-blue-gray-700 outline outline-0 placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-gray-900 focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50",
                'placeholder': " ",
                'minlength' : "8"
            })
    
    context = {
        'form' : signUpForm
    }   
        
    return render(request, 'users/signup.html', context)
    
    
def email_sent_page(request):
        
    return render(request, 'users/email_sent.html')


def management(request):
    users = CustomUser.objects.all()
    page = "user_management"
    
    context = {
        'page_name': page,
        'users': users
    }
    return render(request, 'user_management/index.html', context)