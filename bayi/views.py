import lift
from django.shortcuts import render

from bayi.models import bayi_bilgi
from lift.models import Urun, Siparis


def bayi_bayilist(request):
    return render(request,'bayi/bayi_listesi.html', {})
def bayi_urunsiparis(request):
    return render(request,'bayi/bayi_urun_siparis.html', {})
def bayi_view(request):
    return render(request,'bayi/index.html',{})
def bayi_urunler(request):
    urunler = Urun.objects.all()
    return render(request,'bayi/urunler.html',{'urunler' : urunler,})
def bayi_uruns(request):
    urunler = Urun.objects.all()
    siparis = Siparis.objects.all()
    return render(request,'bayi/uruns.html', {'siparis' : siparis, 'urunler': urunler,})
def bayi_bayidetay(request):
    bayiler = bayi_bilgi.objects.all()
    return render(request,'bayi/bayi_detay.html',{'bayiler' : bayiler,})
def bayi_siparisdetay(request):
    return render(request,'bayi/siparis_detay.html', {})
def bayi_profilduzenle(request):
    bayiler = bayi_bilgi.objects.all()
    return render(request, 'bayi/profil_duzenle.html', {'bayiler': bayiler, })
def bayi_siparis(request):
    return render(request,'bayi/siparis.html',{})
def bayi_bakim(request):
    return render(request,'bayi/bakim.html',{})
def bayi_urunekle(request):
    urunler = Urun.objects.all()
    return render(request,'bayi/urun_ekle.html', {'urunler' : urunler,})
def bayi_siparisozet(request):
    return render(request,'bayi/siparis_ozet.html', {})
def bayi_profil_duzenle(request):
    return render(request,'bayi/profil_duzenle.html', {})
def base(request):
    siparis = Siparis.objects.all()
    urunler = Urun.objects.all()
    return render(request,'bayi/base.html', {'siparis' : siparis, 'urunler': urunler,})