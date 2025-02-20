from django.shortcuts import render, redirect
import json
from .models import (Contact, Permission, Management,get_district)
from django.http import JsonResponse, HttpResponse
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from .serializers import ManagementSerializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home1(request):
    return render(request,"index.html", {"form":'ok'})

def home2(request):
    return render(request, 'base.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) 
        
        if user is not None:
            login(request, user)  
            return redirect('home')  # Redirect to another view (update with your URL name)
        else:
            messages.error(request, "Invalid username or password.")  # Show error message

    return render(request, 'login.html') 

@login_required
def home(request):
    if request.user.is_authenticated:
        district_dict = dict(get_district())
        districts = json.loads(json.dumps(district_dict))  

        user = Permission.objects.get(user=request.user)
        query = request.GET.get("q", "").strip()
        status = request.GET.get("status", "").strip() 

        if status in ["1", "3"]:
            
            managements = Management.objects.filter(type=status)
            print(managements, status)
        else:
            managements = Management.objects.none()

        if user.can_view_all:
            contacts = Contact.objects.all()
        else:
            contacts = Contact.objects.filter(district=user.district)

        serialized_contacts = ContactSerializers(contacts, many=True)

        return render(request, 'indexs.html', {
            'contacts': serialized_contacts.data,
            'query': query,
            'districts': districts,
            'managements': managements  
        })


def get_managements(request):
    status = request.GET.get("status", "").strip()

    if status in ["1", "3"]:
        managements = Management.objects.filter(type=status).values("id", "name")
        return JsonResponse({"valid": True, "data": list(managements)})
    
    return JsonResponse({"valid": False, "data": []})

@csrf_exempt
def check_option_text(request):
    if request.method == "POST":
        status_value = request.POST.get('status_value')
        
        data = Management.objects.filter(type=status_value)
        
        serializer = ManagementSerializers(data, many=True)

        return JsonResponse({'valid': True, 'data': serializer.data})

    return JsonResponse({'valid': False})

