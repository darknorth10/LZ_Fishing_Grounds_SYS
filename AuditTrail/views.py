from django.shortcuts import render
from django.core.paginator import Paginator
from .models import AuditLog
# Create your views here.
def index(request):

    auditlog = AuditLog.objects.all().order_by('-id')
    
    page = "audit"
    
    # pagination
    paginator = Paginator(auditlog, 5) # shows 4 logs per page
    
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    
    # variables rendered to the template
    context = {
        'page_name': page,
        'auditlog': auditlog,
        'page_obj': page_obj,
        'page_char' : 'a' * page_obj.paginator.num_pages
    }

    return render(request, "audit/index.html", context)