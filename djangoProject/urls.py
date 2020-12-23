"""djangoProject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import lift
from bayi.views import bayi_view, bayi_urunekle, bayi_bayilist, bayi_urunsiparis, bayi_urunler, bayi_bayidetay, \
    bayi_siparisdetay, bayi_siparisozet, bayi_siparis
from lift.views import home_view, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name=""),
    path('home',home_view),
    path('bayi/',bayi_view),
    path('bayi/siparis', bayi_siparis),
    path('bayi/urun_ekle', bayi_urunekle),
    path('bayi/bayi_listesi', bayi_bayilist),
    path('bayi/urun_siparis', bayi_urunsiparis),
    path('bayi/urunler', bayi_urunler),
    path('bayi/bayi_detay', bayi_bayidetay),
    path('bayi/siparis_detay', bayi_siparisdetay),
    path('bayi/siparis_ozeti', bayi_siparisozet),
    path('login/', lift.views.login, name='login'),
    path('logout/', lift.views.logout, name='logout')
]

admin.site.site_title = "Liftistan Sistem Yöneticisi"
admin.site.site_header = "Liftistan Admin Paneli"
admin.site.index_title = "Liftistan Admin Paneline Hoşgeldiniz"





