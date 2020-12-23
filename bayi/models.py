from django.db import models

class Bayi_bilgi(models.Model):
    bayis = models.ForeignKey('auth.User', verbose_name='bayis', on_delete=models.CASCADE, related_name='bayis',limit_choices_to={'groups__name': "BayiGrubu"})
    telefon = models.CharField(max_length=100)
    adres = models.TextField()