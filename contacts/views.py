from django.shortcuts import render

from .models import (Contact, Permission, Management)
from django.http import JsonResponse, HttpResponse
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from .serializers import ManagementSerializers
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'index.html')


@csrf_exempt
def check_option_text(request):
    if request.method == "POST":
        status_value = request.POST.get('status_value')
        
        data = Management.objects.filter(type=status_value)
        
        serializer = ManagementSerializers(data, many=True)

        return JsonResponse({'valid': True, 'data': serializer.data})

    return JsonResponse({'valid': False})




# @login_required
# def contact_list(request):
#     permission = Permission.objects.get(user=request.user)
    
#     if request.user.is_superuser or permission.can_view_all:
#         contacts = Contact.objects.all()  # City admin sees all users
#     else:
#         contacts = Contact.objects.filter(district=permission.role.district)  # District admin sees only their users

#     return render(request, "contacts.html", {"contacts": contacts})


def contact_list(reuest):
    data = Contact.objects.all()
    serializers = ContactSerializers(data, many=True)
    return JsonResponse({"ok":serializers.data})