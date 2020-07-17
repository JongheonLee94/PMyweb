from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def mypage(request):
    return render(request, 'mypage.html')
# 출처: https://rednooby.tistory.com/85 [개발자의 취미생활]
# 출처: https: // doorbw.tistory.com / 182?category = 711722[Tigercow.Door]