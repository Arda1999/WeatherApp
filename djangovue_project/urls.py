
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls), #admin sayfasindan kullanici islemlerini yapabiliriz.
    path("accounts/", include("django.contrib.auth.urls")), #kullanici login olmadan, diger sayfalara girisini engellemek icin
    path('', include("weather.urls")) #burada weather app in icinde bulunan url uzantilarini aliyorum ve include ile weather appdeki urlleri projemize ekledim.

]
