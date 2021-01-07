from django.contrib import auth, messages
from django.contrib.auth import authenticate, login as django_logout, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
# Create your views here.
from bayi.models import bayi_bilgi


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
        # bilgiler = Bayi_bilgi(bayis = username, telefon = telefon , adres = adres)
        # bilgiler.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('/bayi/profil_duzenle')
    else:
        return HttpResponseRedirect("/")

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def success(request):
    template = render_to_string('bayi/email.html',{'name':request.user.username})
    email = EmailMessage(
        'Ürün Satın Alınmıştır',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
        )
    email.fail_slienty = False
    email.send()
    return render(request,'bayi/siparis_detay.html')