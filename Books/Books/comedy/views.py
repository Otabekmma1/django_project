from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Komediya bo'limiga xush kelibsiz!</h2>"
                        "<h3>Komediya kitoblar:</h3>"
                        "<p>1.Ur to'qmoq/Бей дубинка</p>"
                        "<p>Nashr yili: 2017</p>"
                        "<p>Janr/bo‘lim: Bolalar adabiyoti, Komediya</p>"
                        "<p>Muallifi: <a href='https://uz.wikipedia.org/wiki/G%CA%BBafur_G%CA%BBulom'>G'ofur G'ulom</a></p>"
                        "<p>Tili: O'zbek (lot)</p>"
                        "<a href='https://kitobsevar.uz/kxpv/xrpt_1x1tryj6o4cvrot881k6f8rg4473jzhal9u4v5yax2vefebd6m0ajphcje6t4dtebd8x9vyvlj1.pdf'>Yuklab olish</a>")
