from django.contrib import admin

# Register your models here.

from django.contrib import admin
from lift.models import Urun,Siparis,Hammadde,Odeme,Recete,Bakim

class UrunlerAdmin(admin.ModelAdmin):
    list_display = ('bayi','urun','adet','tarih') # gösterilecek olan parametreler
    list_filter = ('urun',) #durumuna göre sıralama
    search_fields = ('bayi',) #arama

admin.site.register(Urun)
admin.site.register(Siparis,UrunlerAdmin)
admin.site.register(Hammadde)
admin.site.register(Odeme)
admin.site.register(Recete)
admin.site.register(Bakim)

