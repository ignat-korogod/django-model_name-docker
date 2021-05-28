from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def api(request):
    responseData = {
        'message': 'Hello, world!'
    }

    return JsonResponse(responseData)
