from django.db import models

class bayi_bilgi(models.Model):
    bayis = models.ForeignKey('auth.User', verbose_name='bayis', on_delete=models.CASCADE, related_name='bayis')
    telefon = models.CharField(max_length=100)
    adres = models.TextField()