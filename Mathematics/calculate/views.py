from django.shortcuts import render
from django.http import HttpResponse


def qoshish(request, x, y):
    result = x + y
    return HttpResponse(f"{x} + {y} = {result}")

def ayirish(request, x, y):
    result = x - y
    return HttpResponse(f"{x} - {y} = {result}")

def kopaytirish(request, x, y):
    result = x * y
    return HttpResponse(f"{x} * {y} = {result}")

def bolish(request, x, y):
    if y != 0:
        result = x // y
        return HttpResponse(f"{x} // {y} = {result}")
    else:
        return HttpResponse("Sonni 0 ga bo'lib bo'lmaydi!")
    return HttpResponse(result)
