from django.db import models
from django.utils.safestring import mark_safe


class bayi_bilgi(models.Model):
    bayis = models.ForeignKey('auth.User', verbose_name='bayis', on_delete=models.CASCADE, related_name='bayis')
    telefon = models.CharField(max_length=100)
    adres = models.TextField()
    resim = models.ImageField(blank=True,upload_to='images/')
    def resim_tag(self):
        if self.resim:
                return mark_safe('<img src="{}" height="50"/>'.format(self.resim.url))
        else:
                return ""
    resim_tag.short_description ='Resim'