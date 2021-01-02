from django.contrib import admin
from bayi.models import bayi_bilgi

class BayiAdmin(admin.ModelAdmin):
    list_display = ('bayis', 'resim_tag', )

admin.site.register(bayi_bilgi,BayiAdmin )
