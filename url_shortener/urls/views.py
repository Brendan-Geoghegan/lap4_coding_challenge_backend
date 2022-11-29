from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Urls
from django.core import serializers
import json
import string
import random
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return HttpResponse("Hello")

def list(request):
    urls = Urls.objects.all().first()
    urls_json = jsonify(urls)
    return JsonResponse(urls_json)

def show(request, id):
    if request.method == 'GET':
        url = get_object_or_404(Urls, pk=id)
        url_json = jsonify(url)
        return JsonResponse(url_json)
    

@csrf_exempt
def create(request):
    if request.method == 'POST':
        long_url = json.loads(request.body)
        short_url_path = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        new_url = Urls.objects.create(long_url=long_url["long_url"], short_url=f"http://127.0.0.1:8000/urls/{short_url_path}")
        new_url_json = jsonify(new_url)
        return JsonResponse(new_url_json)



## add this to your db class model
def jsonify(self):
    """ Returns object data in json-compatible dict. """
    jsn = serializers.serialize( 'json', [self] )  # json string is single-item list
    lst = json.loads( jsn )
    object_dct = lst[0]
    return object_dct
