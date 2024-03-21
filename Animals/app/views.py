from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Xush kelibsiz</h2>"
                        "<p>Hayvonlar kategoriyasi:</p>"
                        "<p><a href='cat/'>Mushuk</a></p>"
                        "<p><a href='elephant/'>Fil</a></p>"
                        "<p><a href='monkey/'>Maymun</a></p>")