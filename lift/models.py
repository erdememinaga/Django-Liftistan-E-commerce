from django.db import models
# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Urun(models.Model):
    urun_adi = models.CharField(max_length=100,blank=True)
    urun_aciklama = models.CharField(max_length=100,blank=True)
    # urun_resim = models.ImageField()
    model = models.CharField(max_length=100,blank=True)
    ebat = models.CharField(max_length=100,blank=True)
    fiyat = models.IntegerField()
    fiyat_oran =models.IntegerField(blank=True)
    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'

    def __str__(self):
        return self.urun_adi
class Siparis(models.Model):
    bayi = models.ForeignKey('auth.User', verbose_name='bayi', on_delete=models.CASCADE, related_name='bayi',limit_choices_to={'groups__name': "BayiGrubu"})
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE)
    adet = models.IntegerField()
    tarih = models.DateTimeField()

    class Meta:
        verbose_name = 'Bayi Sipariş'
        verbose_name_plural = 'Bayi Siparişleri'


class Odeme(models.Model):
    bayiler_siparis = models.ForeignKey(Siparis,on_delete=models.CASCADE)
    odeme_turu = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Bayi Ödeme'
        verbose_name_plural = 'Bayi Ödemeleri'

    def __str__(self):
        return self.odeme_turu
class Hammadde(models.Model):

    hammadde_ad = models.CharField(max_length=30)
    temin_sure = models.DateField()
    stok_adet = models.IntegerField()
    fiyat = models.IntegerField()

    class Meta:
        verbose_name = 'Hammadde'
        verbose_name_plural = 'Hammaddeler'

    def __str__(self):
        return self.hammadde_ad

class Recete(models.Model):

    urunler = models.ForeignKey(Urun, on_delete=models.CASCADE)

    #hammadde = models.ForeignKey(Hammadde, on_delete=models.CASCADE)
    hammadde = models.ForeignKey(Hammadde, on_delete=models.CASCADE)
    adet = models.IntegerField()
    char = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Reçete'
        verbose_name_plural = 'Reçeteler'

    def __str__(self):
        return self.urunler

class Bakim(models.Model):

    urunler = models.ForeignKey(Urun,on_delete=models.CASCADE)
    islem_turu = models.CharField(max_length=30)
    maliyet = models.IntegerField()
    sure = models.DateField()
    class Meta:
        verbose_name = 'Bakım'
        verbose_name_plural = 'Bakımlar'


    def __str__(self):
        return self.islem_turu



