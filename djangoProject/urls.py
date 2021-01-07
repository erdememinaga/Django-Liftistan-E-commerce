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
from django.conf import settings
from django.conf.urls.static import static

import lift
from django.contrib import admin
from django.urls import path, include

from bayi.views import bayi_view, bayi_urunekle, bayi_bayilist, bayi_urunsiparis, bayi_urunler, bayi_bayidetay, \
    bayi_siparisdetay, bayi_siparisozet, bayi_siparis, bayi_profil_duzenle, bayi_uruns, bayi_bakim, bayi_profilduzenle
from lift.views import home_view, login, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name=""),
    path('register/', register_view, name="register"),
    path('home', home_view),
    path('bayi/bakim', bayi_bakim),  # özet
    path('bayi/siparis', bayi_siparis),  # siparişlerim
    path('bayi/bayi_listesi', bayi_bayilist),
    path('bayi/urun_siparis', bayi_urunsiparis),  # sepet sayfası
    path('bayi/profil_duzenle', bayi_profilduzenle),  # profil düzenleme
    path('bayi/urunler', bayi_uruns),  # ürünlerim
    path('bayi/urunlerim', bayi_urunler),  # ürünlerim
    path('bayi/bayi_detay', bayi_bayidetay),  # profil
    path('bayi/siparis_detay', bayi_siparisdetay),  # sipariş detayları
    path('bayi/siparis_ozeti', bayi_siparisozet),
    path('login/', lift.views.login, name='login'),
    path('logout/', lift.views.logout, name='logout'),
    path('singup/', lift.views.singup, name='singup'),
    path('success/',lift.views.success, name='success'),
    path('profilduzen/<bayis_id>',lift.views.profilduzen,name='profilduzen'),

    path('sepete_ekle/', lift.views.sepete_ekle, name='sepete_ekle'),
    path('delete/<id>',lift.views.delete,name='delete')
]

admin.site.site_title = "Liftistan Sistem Yöneticisi"
admin.site.site_header = "Liftistan Admin Paneli"
admin.site.index_title = "Liftistan Admin Paneline Hoşgeldiniz"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
