from django.shortcuts import render

def bayi_bayilist(request):
    return render(request,'bayi/bayi_listesi.html', {})
def bayi_urunsiparis(request):
    return render(request,'bayi/bayi_urun_siparis.html', {})
def bayi_view(request):
    return render(request,'bayi/index.html',{})
def bayi_urunler(request):
    return render(request,'bayi/urunler.html',{})
def bayi_uruns(request):
    return render(request,'bayi/uruns.html',{})
def bayi_bayidetay(request):
    return render(request,'bayi/bayi_detay.html',{})
def bayi_siparisdetay(request):
    return render(request,'bayi/siparis_detay.html', {})
def bayi_profilduzenle(request):
    return render(request,'bayi/profil_duzenle.html', {})
def bayi_siparis(request):
    return render(request,'bayi/siparis.html',{})
def bayi_urunekle(request):
    return render(request,'bayi/urun_ekle.html', {})
def bayi_siparisozet(request):
    return render(request,'bayi/siparis_ozet.html', {})
def bayi_profil_duzenle(request):
    return render(request,'bayi/profil_duzenle.html', {})

