from django.db import models

# Create your models here.


class Modeller(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )

    model_ad = models.CharField(max_length=30)
    #urunler = models.ForeignKey(Urunler,on_delete=models.CASCADE)


    def __str__(self):
        return self.model_ad


class Ebat(models.Model):
    ebat_ad = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Ebat'
        verbose_name_plural = 'Ebatlar'

    def __str__(self):
        return self.ebat_ad


class Urunler(models.Model):
    STATUS =(
        ('True','Evet'),
        ('False','Hayır'),
    )

    urun_ad = models.CharField(max_length=50)
    #model = models.ForeignKey(Modeller,on_delete=models.CASCADE)
    ebat = models.ForeignKey(Ebat,on_delete=models.CASCADE)
    fiyat = models.IntegerField()
    status = models.CharField(max_length=10,choices=STATUS)
    slug = models.SlugField()
    #parent = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
   # modeller = models.ForeignKey(Modeller, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'


    def __str__(self):
        return self.urun_ad


class Bakim(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    urunler = models.ForeignKey(Urunler,on_delete=models.CASCADE)
    islem_turu = models.CharField(max_length=30)
    maliyet = models.IntegerField()
    sure = models.TimeField()
    class Meta:
        verbose_name = 'Bakım'
        verbose_name_plural = 'Bakımlar'


    def __str__(self):
        return self.islem_turu





class Hammadde(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    #urunler = models.ForeignKey(Urunler, on_delete=models.CASCADE)
    #hammadde = models.ForeignKey(Hammadde, on_delete=models.CASCADE)
    hammadde_ad = models.CharField(max_length=30)
    temin_sure = models.TimeField()
    stok_adet = models.IntegerField()
    fiyat = models.IntegerField()

    class Meta:
        verbose_name = 'Hammadde'
        verbose_name_plural = 'Hammaddeler'

    def __str__(self):
        return self.hammadde_ad

class Recete(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    urunler = models.ForeignKey(Urunler, on_delete=models.CASCADE)

    #hammadde = models.ForeignKey(Hammadde, on_delete=models.CASCADE)
    hammadde = models.ForeignKey(Hammadde, on_delete=models.CASCADE)
    kullanim = models.TextField()

    class Meta:
        verbose_name = 'Reçete'
        verbose_name_plural = 'Reçeteler'

    # def __str__(self):
    #     return self.islem_tur

class Bayiler(models.Model):
    bayi_ad = models.CharField(max_length=30)
    bayi_adres = models.CharField(max_length=50)
    bayi_tel = models.CharField(max_length=30)
    bayi_mail = models.CharField(max_length=30)
    sifre = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Bayi'
        verbose_name_plural = 'Bayiler'

    def __str__(self):
        return self.bayi_ad


class Bayiler_Siparis(models.Model):

    bayiler = models.ForeignKey(Bayiler,on_delete=models.CASCADE)
    urunler = models.ForeignKey(Urunler, on_delete=models.CASCADE)
    adet = models.IntegerField()
    tarih = models.DateTimeField()

    class Meta:
        verbose_name = 'Bayi Sipariş'
        verbose_name_plural = 'Bayi Siparişleri'
    #
    # def __str__(self):
    #     return self.


class Bayiler_Odeme(models.Model):
    bayiler_siparis = models.ForeignKey(Bayiler_Siparis,on_delete=models.CASCADE)
    odeme_turu = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Bayi Ödeme'
        verbose_name_plural = 'Bayi Ödemeleri'

    def __str__(self):
        return self.odeme_turu







