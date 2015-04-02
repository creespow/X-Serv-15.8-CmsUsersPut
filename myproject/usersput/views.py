from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import cars
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def login(request):
    if request.user.is_authenticated():
        return (" " + request.user.username)
    else:
        return ("<br><br>You arent logged <a href='/admin/login/'>Login</a><br>")

def all(request):
    cars_list = cars.objects.all()
    out = "<ul>\n"
    for fila in cars_list:
        out += "<li><a href=/" + fila.model +  " > " + fila.model + "</a></li>\n"
    out += "</ul\n"
    out += login(request)
    return HttpResponse(out)

@csrf_exempt
def info (request, resource):
    if request.method == 'GET':
        cars_list = cars.objects.filter(model=resource)
        if not cars_list:
            return notfound (request, resource)
        out = ""
        for car in cars_list:
            out += car.model + ": " + str(car.price) + " $"
        out += login(request)
        return HttpResponse(out)
    elif request.method == 'PUT':
        if request.user.is_authenticated():
            newCar = cars(model = resource, price = request.body)
            newCar.save()
            out = "Saved"
        else:
            out = "You arent logged"
    out += login (request)
    return HttpResponse (out)

def notfound (request, resource):
    out = ("Not found: " + resource)
    out += login(request)
    return HttpResponseNotFound(out)
