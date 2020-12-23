from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from lift.models import Urun,Siparis,Hammadde,Odeme,Recete,Bakim,models





class UrunlerAdmin(admin.ModelAdmin):
    list_display = ('bayi','urun','adet','tarih') # gösterilecek olan parametreler
    list_filter = ('urun',) #durumuna göre sıralama
    search_fields = ('bayi',) #arama

class User(admin.ModelAdmin):
    list_display = ('')


admin.site.register(Urun)
admin.site.register(Siparis,UrunlerAdmin)
admin.site.register(Hammadde)
admin.site.register(Odeme)
admin.site.register(Recete)
admin.site.register(Bakim)

