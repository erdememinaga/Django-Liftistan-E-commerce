from django.contrib import admin

# Register your models here.

class UrunlerAdmin(admin.ModelAdmin):
    list_display = ('urun_ad','ebat','fiyat') # gösterilecek olan parametreler
    list_filter = ('status',) #durumuna göre sıralama
    ordering = ('urun_ad','-update_at') #sıralama
    search_fields = ('urun_ad',) #arama
    prepopulated_fields = {'slug':('urun_ad',)} #başlıkla bağlantılı slug
    list_per_page = 20 # sayfa başına kaç madde geleceği


from.models import Urunler,Bayiler,Bakim,Hammadde,Recete,Bayiler_Siparis,Bayiler_Odeme,Ebat
admin.site.register(Urunler,UrunlerAdmin)
admin.site.register(Bayiler)
admin.site.register(Bakim)
admin.site.register(Hammadde)
admin.site.register(Recete)
admin.site.register(Bayiler_Siparis)
admin.site.register(Bayiler_Odeme)
admin.site.register(Ebat)