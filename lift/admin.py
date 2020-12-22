from django.contrib import admin

# Register your models here.

from django.contrib import admin
from lift.models import Urun,Siparis,Hammadde,Odeme,Recete,Bakim

admin.site.register(Urun)
admin.site.register(Siparis)
admin.site.register(Hammadde)
admin.site.register(Odeme)
admin.site.register(Recete)
admin.site.register(Bakim)