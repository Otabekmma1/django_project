from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Detektiv kitoblar bo'limiga xush kelibsiz!</h2>"
                        "<h3>Detektiv kitoblar:</h3>"
                        "<p>1.O'g'irlangan bolalik</p>"
                        "<p>Nashr yili: 2021</p>"
                        "<p>Janr/bo‘lim: Detektiv</p>"
                        "<p>Muallifi: <a href='https://teletype.in/@mmuratov/--XvA80IMws'>Sindarov Komil</a></p>"
                        "<p>Tili: O'zbek (lot)</p>"
                        "<a href='https://packpdf.com/books/11102-komil-sindarov-ogirlangan-bolalik/download'>Yuklab olish</a>")
