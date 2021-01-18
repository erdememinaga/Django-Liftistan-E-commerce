from django.contrib import auth, messages
from django.contrib.auth import authenticate, login as django_logout, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group, User
# Create your views here.
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bayi.models import bayi_bilgi
from lift.models import Siparis, Bakim, Odeme,Urun,Recete,Hammadde
from lift.serializers import SiparisSerializers,BakimSerializers


@api_view(['GET', 'POST'])
def snippet_list(request,format='Accept' ):

    if request.method == 'GET':
        snippets = Siparis.objects.all()
        serializer = SiparisSerializers(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SiparisSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST'])
def bakim_snippet_list(request,format='Accept' ):

    if request.method == 'GET':
        snippets = Bakim.objects.all()
        serializer = BakimSerializers(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BakimSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk,format='Accept'):

    try:
        snippet = Siparis.objects.get(pk=pk)
    except Siparis.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SiparisSerializers(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SiparisSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def bakim_snippet_detail(request, pk,format='Accept'):

    try:
        snippet = Bakim.objects.get(pk=pk)
    except Bakim.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BakimSerializers(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BakimSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def home_view(request):

    return render(request, 'login.html',{})

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                users_in_group = Group.objects.get(name="BayiGrubu").user_set.all()

                if user in users_in_group:
                    auth.login(request,user)
                    return redirect('/bayi/bayi_detay')
                else:
                    auth.login(request,user)
                    return redirect('/admin/')

            else:
                messages.info(request, 'Şifre veya kullanıcı adı yanlış')
                return HttpResponseRedirect("/")
        else:

            messages.info(request, 'Şifre veya kullanıcı adı yanlış')
            return HttpResponseRedirect("/")
    else:
        messages.info(request, 'Şifre veya kullanıcı adı yanlış')
        return HttpResponseRedirect("/")

@login_required
def logout(request):
    print('logged out')
    auth.logout(request)

    return redirect('')
def musteri_fiyat(request):
    if request.method == "POST":
        musteri_fiyat = request.POST["musteri_fiyat"]
        musteri_fiyat = int(musteri_fiyat)
        urun = request.POST['urun']
        id = request.user.id
        a = Siparis.objects.filter(urun_id=urun, bayi_id=id )

        a.update(fiyat_oran=musteri_fiyat)
        url = '../bayi/urunlerim'
        resp_body = '<script>alert("Fiyat Güncellendi!");\
                         window.location="%s"</script>' % url
        return HttpResponse(resp_body)


def register_view(request):
    return render(request, 'register.html',{})


def singup(request):
    if request.method == "POST":
        username = request.POST["username"]
        isim = request.POST["isim"]
        soyisim = request.POST["soyisim"]

        # telefon = request.POST["telefon"]
        email = request.POST["email"]
        password_check = request.POST["password_check"]
        password = request.POST["password"]
        # adres = request.POST["adres"]

        if (password != password_check):
            messages.error(request, " Passwords do not match")
            return redirect('')
        group = Group.objects.get(name="BayiGrubu")
        user = User.objects.create_user(username,email,password)
        group.user_set.add(user)
        user.first_name = isim
        user.last_name = soyisim
        user.save()
        auth.login(request,user)
        bilgiler = bayi_bilgi(bayis_id=user.id, telefon=isim, adres=soyisim)
        bilgiler.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('/bayi/profil_duzenle')
    else:
        return HttpResponseRedirect("/")

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def success(request):
    if request.method == 'POST':
        yontem = request.POST['yontem']
        urundizi={}

        siparisler = Siparis.objects.filter(bayi_id=request.user.id, STATUS=0)
        for rs in siparisler:
            siparis = int(rs.id)
            odeme = Odeme(odeme_turu=yontem, bayiler_siparis_id=siparis)
            odeme.save()

            urunler = Urun.objects.get(id=rs.urun.id)
            urunler.stok -= rs.adet
            urunler.save()
            urundizi[urunler.urun_adi] = rs.adet


            recete = Recete.objects.filter(urunler_id=rs.urun.id)
            for rc in recete:

                id =int(rc.hammadde_id)
                hammade =Hammadde.objects.get(id=id)
                hammade.stok_adet-=rs.adet * rc.adet
                hammade.save()


    template = render_to_string('bayi/email.html', {'name': request.user.username,'urun':urundizi})
    email = EmailMessage(
        'Ürün Satın Alınmıştır',
        template,
        settings.EMAIL_HOST_USER,
        ['bera.cay@hotmail.com'],
    )
    email.fail_slienty = False
    email.send()
    ham = Hammadde.objects.all()
    hamdizi = {}
    for ham in ham:
        if ham.stok_adet <= 20:
            hamdizi[ham.hammadde_ad] = ham.stok_adet

    template = render_to_string('bayi/hammail.html', {'hamdizi': hamdizi})
    email = EmailMessage(
        'Dikkat hammadde azalmaktadır.',
        template,
        settings.EMAIL_HOST_USER,
        ['bera.cay@hotmail.com'],
    )
    email.fail_slienty = False
    email.send()

    id = request.user.id
    siparis = Siparis.objects.filter(bayi_id=id, STATUS=0)
    siparis.update(STATUS=2, tarih=timezone.now())
    url = '../bayi/urunlerim'
    resp_body = '<script>alert("Ödemeniz Alındı!");\
                 window.location="%s"</script>' % url
    return HttpResponse(resp_body)





@login_required()
@login_required()
def sepete_ekle(request):
    if  request.method == 'POST':
        urun = request.POST[ "urun" ]
        siparis_adet = request.POST["adet"]
        status = 0
        fiyat_oran = 0
        id = request.user.id


        try:
            a = Siparis.objects.filter(urun_id=urun,bayi_id=id,STATUS=status)
            b = get_object_or_404(Siparis, urun_id=urun,bayi_id=id,STATUS=status)
            a.update(adet=int(siparis_adet) + int(b.adet))
        except:
            urunler = Siparis(bayi_id=id, urun_id=urun, STATUS=status, adet=siparis_adet, tarih=timezone.now(),fiyat_oran=fiyat_oran)
            urunler.save()





        return redirect('/bayi/urunler')
    else:
        return HttpResponseRedirect("/")

def delete(request,id):
    print("silindi")
    getir = Siparis.objects.filter(id = id)
    getir.delete()

    return redirect('/bayi/urunler')

def profilduzen(request,bayis_id):
    if request.method == "POST":
        id = request.user.id
        telefon = request.POST["telefon"]
        adres = request.POST["adres"]
        getir=bayi_bilgi.objects.filter(bayis_id=id)
        getir.update(telefon=telefon,adres=adres)

        return redirect('../bayi/profil_duzenle')

    return redirect('/bayi/urunler')

