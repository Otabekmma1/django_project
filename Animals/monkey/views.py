from django.http import HttpResponse

def index(reauest):
    return HttpResponse("<h2>Maymunlar bo'limiga xush kelibsiz</h2>"
                        "<p>1.Maymun</p>"
                        "<p>Narxi: 5000$</p>"
                        "<p><a href='buy/'>Sotib olish</a></p>")

def buy(request):
    return HttpResponse("Xaridingiz uchun rahmat!")