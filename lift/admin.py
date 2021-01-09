from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from lift.models import Urun,Siparis,Hammadde,Odeme,Recete,Bakim,Images

class UrunlerResimInline(admin.TabularInline):
    model = Images
    extra = 3

class UrunlerAdmin(admin.ModelAdmin):
    list_display = ('urun_adi', 'image_tag', 'model', 'fiyat')  # gösterilecek olan parametreler
    search_fields = ('urun_adi',)  # arama
    inlines = [UrunlerResimInline]
    readonly_fields = ('image_tag',)

class SiparisAdmin(admin.ModelAdmin):
    list_display = ('bayi','urun','adet','tarih','STATUS',) # gösterilecek olan parametreler
    list_filter = ('urun',) #durumuna göre sıralama
    readonly_fields = ('bayi','urun','adet','tarih',)
    search_fields = ('bayi',) #arama


class User(admin.ModelAdmin):
    list_display = ('')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('urunler','baslik','resim') # gösterilecek olan parametreler
    search_fields = ('urunler',) #arama

admin.site.register(Urun,UrunlerAdmin)
admin.site.register(Siparis,SiparisAdmin)
admin.site.register(Hammadde)
admin.site.register(Odeme)
admin.site.register(Recete)
admin.site.register(Bakim)
#admin.site.register(Images,ImageAdmin)

