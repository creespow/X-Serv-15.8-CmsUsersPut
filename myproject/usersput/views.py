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
        out += "<li><a href=id/" + fila.model +  " > " + fila.model + "</a></li>\n"
    out += "</ul\n"
    out += login(request)
    return HttpResponse(out)

@csrf_exempt
def info (request, car):
    if request.method == 'GET':        
        out = ""
        try:
            one_car = cars.objects.get(model = car)
            out += one_car.model + ": " + str(one_car.price) + "$"
        except:
            out += "No cars, add to DB"
        out += login(request)
        return HttpResponse(out)
    elif request.method == 'PUT':
        if request.user.is_authenticated():
            newCar = cars(model = car, price = request.body)
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
