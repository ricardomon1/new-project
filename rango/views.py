from django.shortcuts import render

from django.http import HttpResponse

def index(request):
<<<<<<< HEAD
    context_dict= {"boldmesage":Crunchy, creamy, cookie, candy, cupcake}
    #return HttpResponse("Rango say here")
    return render(request, ' rango/index.html,'context=context_dict)

def about(request):
    return HttpResponse("rango says here about page")
=======
    return HttpResponse("Rango say here")
>>>>>>> main
