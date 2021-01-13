from django.db.models import Sum

import lift
from django.shortcuts import render

from bayi.models import bayi_bilgi
from lift.models import Urun, Siparis


def bayi_bayilist(request):
    siparis = Siparis.objects.all()
    bayiler = bayi_bilgi.objects.all()
    urunler = Urun.objects.all()
    return render(request,'bayi/bayi_listesi.html', {'bayiler':bayiler,'siparis':siparis,'urunler':urunler})
def bayi_urunsiparis(request):
    siparis = Siparis.objects.all()
    bayiler = bayi_bilgi.objects.all()
    urunler = Urun.objects.all()
    return render(request,'bayi/bayi_urun_siparis.html',{'bayiler':bayiler,'siparis':siparis,'urunler':urunler})
def bayi_view(request):
    siparis = Siparis.objects.all()
    bayiler = bayi_bilgi.objects.all()
    urunler = Urun.objects.all()
    return render(request,'bayi/index.html',{'bayiler':bayiler,'siparis':siparis,'urunler':urunler})
def bayi_urunler(request):
    siparis = Siparis.objects.all()
    bayiler = bayi_bilgi.objects.all()
    urunler = Urun.objects.all()
    b = Siparis.objects.filter(bayi=request.user,STATUS=2).aggregate(Sum("adet"))['adet__sum'] or 0
    os = Siparis.objects.filter(bayi=request.user, STATUS=1).aggregate(Sum("adet"))['adet__sum'] or 0
    ts = Siparis.objects.filter(bayi=request.user, STATUS=3).aggregate(Sum("adet"))['adet__sum'] or 0
    return render(request,'bayi/urunler.html',{'bayiler':bayiler,'siparis':siparis,'urunler':urunler,'b':b,'os':os,'ts':ts})
def bayi_uruns(request):
    siparis = Siparis.objects.all()
    bayiler = bayi_bilgi.objects.all()
    urunler = Urun.objects.all()
    return render(request,'bayi/uruns.html', {'siparis' : siparis, 'urunler': urunler,})
def bayi_bayidetay(request):

    siparis = Siparis.objects.all()
    urunler = Urun.objects.all()
    bayiler = bayi_bilgi.objects.all()


    a = Siparis.objects.filter(bayi=request.user).aggregate(Sum("adet"))['adet__sum'] or 0.00
    return render(request,'bayi/bayi_detay.html',{'bayiler':bayiler,'siparis':siparis,'urunler':urunler, 'a': a})

def bayi_siparisdetay(request):
    siparis = Siparis.objects.all()
    bayiler = bayi_bilgi.objects.all()
    urunler = Urun.objects.all()
    total = 0
    c = Siparis.objects.filter( bayi_id=request.user, STATUS=0)
    for c in c:
        total += c.urun.fiyat * c.adet

    return render(request,'bayi/siparis_detay.html', {'bayiler':bayiler,'siparis':siparis,'urunler':urunler,'total':total})
def bayi_profilduzenle(request):
    siparis = Siparis.objects.all()
    bayiler = bayi_bilgi.objects.all()
    urunler = Urun.objects.all()
    return render(request, 'bayi/profil_duzenle.html', {'bayiler':bayiler,'siparis':siparis,'urunler':urunler})
def bayi_siparis(request):
    siparis = Siparis.objects.all()
    bayiler = bayi_bilgi.objects.all()
    urunler = Urun.objects.all()
    return render(request,'bayi/siparis.html',{'bayiler':bayiler,'siparis':siparis,'urunler':urunler})
def bayi_bakim(request):
    siparis = Siparis.objects.all()
    bayiler = bayi_bilgi.objects.all()
    urunler = Urun.objects.all()
    return render(request,'bayi/bakim.html',{'bayiler':bayiler,'siparis':siparis,'urunler':urunler})
def bayi_urunekle(request):
    siparis = Siparis.objects.all()
    bayiler = bayi_bilgi.objects.all()
    urunler = Urun.objects.all()
    return render(request,'bayi/urun_ekle.html', {'bayiler':bayiler,'siparis':siparis,'urunler':urunler})
def bayi_siparisozet(request):
    siparis = Siparis.objects.all()
    bayiler = bayi_bilgi.objects.all()
    urunler = Urun.objects.all()
    return render(request,'bayi/siparis_ozet.html', {'bayiler':bayiler,'siparis':siparis,'urunler':urunler})
def bayi_profil_duzenle(request):
    siparis = Siparis.objects.all()
    bayiler = bayi_bilgi.objects.all()
    urunler = Urun.objects.all()
    return render(request,'bayi/profil_duzenle.html', {'bayiler':bayiler,'siparis':siparis,'urunler':urunler})
