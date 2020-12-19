from django.contrib import admin

# Register your models here.
from.models import Urunler
admin.site.register(Urunler)

# from.models import Modeller
# admin.site.register(Modeller)
from.models import Bayiler,Bakim,Hammadde,Recete,Bayiler_Siparis,Bayiler_Odeme,Ebat
admin.site.register(Bayiler)
admin.site.register(Bakim)
admin.site.register(Hammadde)
admin.site.register(Recete)
admin.site.register(Bayiler_Siparis)
admin.site.register(Bayiler_Odeme)
admin.site.register(Ebat)