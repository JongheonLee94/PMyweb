from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('mypage/', views.mypage),
]

# 출처: https: // doorbw.tistory.com / 182?category = 711722[Tigercow.Door]