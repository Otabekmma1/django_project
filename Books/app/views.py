from django.http import HttpResponse

def index(request):
    return HttpResponse("<h3>Xush kelibsiz!</h3>"
                        "<p>Ushbu saytda kitoblar haqida ma'lumot olishingiz yoki yuklab olishingiz mumkin.</p>"
                        "<p>Kategoriyalar:</p>"
                        "<p><a href='comedy/'>Komediya</a></p>"
                        "<p><a href='detective/'>Detektiv</a></p>"
                        "<p><a href='bestseller/'>Eng ko'p sotilgan kitoblar</a></p>")