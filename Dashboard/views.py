from django.shortcuts import render

# Create your views here.
def index(request):
    page = "dashboard"
    
    
    context = {
        'page_name' : page
    }
    return render(request, 'dashboard/index.html', context)