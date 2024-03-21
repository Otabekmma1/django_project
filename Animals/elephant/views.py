from django.http import HttpResponse

def index(reauest):
    return HttpResponse("<h2>Fillar bo'limiga xush kelibsiz</h2>"
                        "<p>1.Fil</p>"
                        "<p>Narxi: 10000$</p>"
                        "<p><a href='buy/'>Sotib olish</a></p>")

def buy(request):
    return HttpResponse("Xaridingiz uchun rahmat!")