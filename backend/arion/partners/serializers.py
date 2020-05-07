from .models import Partner
from rest_framework import serializers

class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
