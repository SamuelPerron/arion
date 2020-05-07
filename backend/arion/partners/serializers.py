from .models import Partner, Contact
from arion.common.serializers import AddressSerializer
from rest_framework import serializers

class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Partner
        fields = '__all__'

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
