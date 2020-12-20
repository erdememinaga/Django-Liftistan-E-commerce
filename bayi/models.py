# from django.db import models
#
# # Create your models here.
#
#
# class Modeller(models.Model):
#     STATUS = (
#         ('True', 'Evet'),
#         ('False', 'Hayır'),
#     )
#
#     model_ad = models.CharField(max_length=30)
#     #urunler = models.ForeignKey(Urunler,on_delete=models.CASCADE)
#
#
#     def _str_(self):
#         return self.model_ad
#
#
# class Ebat(models.Model):
#     ebat_ad = models.CharField(max_length=30)
#
#     def _str_(self):
#         return self.ebat_ad
#
#
# class Urunler(models.Model):
#     STATUS =(
#         ('True','Evet'),
#         ('False','Hayır'),
#     )
#
#     urun_ad = models.CharField(max_length=50)
#     #model = models.ForeignKey(Modeller,on_delete=models.CASCADE)
#     ebat = models.ForeignKey(Ebat,on_delete=models.CASCADE)
#     fiyat = models.IntegerField()
#     status = models.CharField(max_length=10,choices=STATUS)
#     slug = models.SlugField()
#     #parent = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#    # modeller = models.ForeignKey(Modeller, on_delete=models.CASCADE)
#
#
#     def _str_(self):
#         return self.urun_ad
#
#
# class Bakim(models.Model):
#     STATUS = (
#         ('True', 'Evet'),
#         ('False', 'Hayır'),
#     )
#     urunler = models.ForeignKey(Urunler,on_delete=models.CASCADE)
#     islem_turu = models.CharField(max_length=30)
#     maliyet = models.IntegerField()
#     sure = models.TimeField()
#
#
#     def _str_(self):
#         return self.islem_turu
#
#
#
#
#
# class Hammadde(models.Model):
#     STATUS = (
#         ('True', 'Evet'),
#         ('False', 'Hayır'),
#     )
#     #urunler = models.ForeignKey(Urunler, on_delete=models.CASCADE)
#     #hammadde = models.ForeignKey(Hammadde, on_delete=models.CASCADE)
#     hammadde_ad = models.CharField(max_length=30)
#     temin_sure = models.TimeField()
#     stok_adet = models.IntegerField()
#     fiyat = models.IntegerField()
#
#     def _str_(self):
#         return self.hammadde_ad
#
# class Recete(models.Model):
#     STATUS = (
#         ('True', 'Evet'),
#         ('False', 'Hayır'),
#     )
#     urunler = models.ForeignKey(Urunler, on_delete=models.CASCADE)
#
#     #hammadde = models.ForeignKey(Hammadde, on_delete=models.CASCADE)
#     hammadde = models.ForeignKey(Hammadde, on_delete=models.CASCADE)
#     kullanim = models.CharField(max_length=50)
#
#     # def _str_(self):
#     #     return self.islem_tur
#
# class Bayiler(models.Model):
#     bayi_ad = models.CharField(max_length=30)
#     bayi_adres = models.CharField(max_length=50)
#     bayi_tel = models.CharField(max_length=30)
#     bayi_mail = models.CharField(max_length=30)
#     sifre = models.CharField(max_length=30)
#
#     def _str_(self):
#         return self.bayi_ad
#
#
# class Bayiler_Siparis(models.Model):
#     #urunler = models.ForeignKey(Urunler,on_delete=models.CASCADE)
#     bayiler = models.ForeignKey(Bayiler,on_delete=models.CASCADE)
#     adet = models.IntegerField()
#     tarih = models.DateTimeField()
#
#
#
# class Bayiler_Odeme(models.Model):
#     bayiler_siparis = models.ForeignKey(Bayiler_Siparis,on_delete=models.CASCADE)
#     odeme_turu = models.CharField(max_length=30)
#
#     def _str_(self):
#         return self.odeme_turu
