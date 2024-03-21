from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Eng ko'p sotilgan kitoblar bo'limiga xush kelibsiz!</h2>"
                        "<p>1.Uzuklar hukmdori</p>"
                        "<p>Nashr yili: 1954-1955</p>"
                        "<p>Janr/bo‘lim: Fantastik</p>"
                        "<p>Muallifi: <a href='https://uz.wikipedia.org/wiki/J._R._R._Tolkien'>J.R.R.Tolken</a></p>"
                        "<p>Tili: Ingliz</p>"
                        "<p>Sotilish: 150 mln</p>"
                        "<a href='https://lib.fbtuit.uz/assets/files/JON-RONALDUZUKLARHUKMDORITOSHKENT2019.pdf'>Yuklab olish</a>")
