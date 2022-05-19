from unicodedata import category
from django.shortcuts import render

from django.http import HttpResponse

from rango.models import Category

def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}

    context_dict= {"boldmesage":'Crunchy, creamy, cookie, candy, cupcake'}
    context_dict['categories']= category_list
    #return HttpResponse("Rango say here")
    return render(request, 'rango/index.html',context=context_dict)

def about(request):
    return HttpResponse("rango says here about page")

    #return HttpResponse("Rango say here")
