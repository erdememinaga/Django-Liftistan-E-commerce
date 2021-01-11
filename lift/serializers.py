from rest_framework import serializers
from .models import Siparis,Bakim
class SiparisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Siparis

        fields = '__all__'

class BakimSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bakim

        fields = '__all__'