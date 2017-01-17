from django.http import HttpResponse
from django.shortcuts import render
from .models import Cafe

def index(request):
    # return HttpResponse("Hello, world. You're at the index.")

    cafe_list = Cafe.objects.all()
    name = "Brad"
    return render(request, "index.html", {"cafe_list": cafe_list})
