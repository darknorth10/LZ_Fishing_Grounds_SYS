from django.shortcuts import get_object_or_404, redirect, render
from .models import CustomUser
from .forms import CustomUserCreationForm, NewUserForm, SignInForm, CustomUserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
# sign in view
def index(request):
    signInForm = SignInForm()
    signUpForm = CustomUserCreationForm()
    page_name = "index"
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
                    else:
                        return redirect('dashboard')
                    
                else:
                    print("Error")
                    message = "Incorrect username or password."
                    
                    
            else:
                signInForm = SignInForm()
                message = "Invalid values"
                
                       
    
    
    return render(request, 'index.html', context={'form' : signInForm, 'err': message, 'form2' : signUpForm, 'page_name': page_name})



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
            signUpForm.role = "customer"
            
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
    

# successfull sign up and email verification page
def email_sent_page(request):
        
    return render(request, 'users/email_sent.html')


# User management view
def management(request):
    # users object
    users = CustomUser.objects.all().order_by('-id')
    
    if request.GET.get("search"):
        if request.GET.get("search") is not None:
          
            search = request.GET.get("search")
            users = CustomUser.objects.filter(Q(username__icontains=search) | Q(email__icontains=search) | Q(last_name__icontains=search)).order_by('-id')
    page = "user_management"
    
    # pagination
    paginator = Paginator(users, 5) # shows 4 users per page
    
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    
    # variables rendered to the template
    context = {
        'page_name': page,
        'users': users,
        'page_obj': page_obj,
        'page_char' : 'a' * page_obj.paginator.num_pages
    }
    
    return render(request, 'user_management/index.html', context)

# User management view_all
def view_all(request):
    # users object
    users = CustomUser.objects.all().order_by('-id')
    
    page = "user_management"
    
    # variables rendered to the template
    context = {
        'page_name': page,
        'users': users,
    }
    
    return render(request, 'user_management/view_all.html', context)


# add user page 
def new_user_page(request):
    new_user_form = NewUserForm()
    
    if request.method == "POST":
        new_user_form = NewUserForm(request.POST)
        
        if new_user_form.is_valid():
            new_user_form.save()
            messages.add_message(request, messages.SUCCESS, "New user has been registered successfully.")
            return redirect('user_management')   
          
        else:
            messages.add_message(request, messages.ERROR, "Error creating user.")
        
    new_user_form.fields['password1'].widget.attrs.update({
                'class': "w-full h-full px-3 py-3 font-sans text-sm font-normal transition-all bg-transparent border rounded-md peer border-blue-gray-200 border-t-transparent text-blue-gray-700 outline outline-0 placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-gray-900 focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50",
                'placeholder': " ",
                'minlength' : "8"
            })
    new_user_form.fields['password2'].widget.attrs.update({
                'class': "w-full h-full px-3 py-3 font-sans text-sm font-normal transition-all bg-transparent border rounded-md peer border-blue-gray-200 border-t-transparent text-blue-gray-700 outline outline-0 placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-gray-900 focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50",
                'placeholder': " ",
                'minlength' : "8"
            }) 
    
     
    context = {
        'form': new_user_form,
    }
    
    return render(request, 'user_management/new_user.html', context)


# update user page

def update_user_page(request, id):
    # user = CustomUser.objects.get(id=id)
    
    obj = get_object_or_404(CustomUser, id = id)
   
    form = CustomUserChangeForm(request.POST or None, instance = obj)
    
    if request.method == "POST":
        
        if form.is_valid():
          
          form.save()
          
          return redirect('user_management')
      
        else:
            
            print(form.errors) 

    context = {
        'form' : form
    }
    
    return render(request, 'user_management/update_user.html', context)



    