from django.shortcuts import render

from .models import (Contact,Permission,Management,Role)
from django.http import JsonResponse, HttpResponse
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from .serializers import ManagementSerializers

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



