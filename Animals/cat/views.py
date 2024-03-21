from django.http import HttpResponse

def index(reauest):
    return HttpResponse("<h2>Mushuklar bo'limiga xush kelibsiz</h2>"
                        "<p>1.Britaniya mushugi</p>"
                        "<p>Narxi: 200$</p>"
                        "<p><a href='buy/'>Sotib olish</a></p>")

def buy(request):
    return HttpResponse("Xaridingiz uchun rahmat!")