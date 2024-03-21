from django.shortcuts import render
from django.http import HttpResponse

def text(request):
    return HttpResponse('<h3>      Xush kelibsiz!</h3>'
                        '<p>Ushbu saytda 2 ta sonni:</p>'
                        '<p>1.qoshish  ------> http://127.0.0.1:8000/calculate/add/1-son/2-son/</p>'
                        '<p>2.ayirish  ------> http://127.0.0.1:8000/calculate/subtract/1-son/2-son/</p>'
                        '<p>3.kopaytirish  ------> http://127.0.0.1:8000/calculate/multiply/1-son/2-son/</p>'
                        '<p>4.bolishingiz mumkin ------> http://127.0.0.1:8000/calculate/divide/1-son/2-son/</p>')