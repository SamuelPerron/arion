from .models import Partner, Contact
from .serializers import PartnerSerializer, ContactSerializer
from rest_framework import viewsets


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
