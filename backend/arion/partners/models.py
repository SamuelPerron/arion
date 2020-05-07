from django.db import models
from django.core.validators import RegexValidator
from arion.common.models import Address

class Partner(models.Model):
    logo = models.ImageField(upload_to='uploads/partner/logos/', blank=True)
    name = models.CharField(max_length=255)
    internal_code = models.CharField(max_length=64, blank=True)
    company_number = models.CharField(max_length=8, blank=True)
    website = models.CharField(max_length=255, blank=True)
    internal_notes = models.TextField(blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.internal_code:
            code = f'[{self.internal_code}] '
        else:
            code = ''
        return f'{code}{self.name}'


class Contact(models.Model):
    name = models.CharField(max_length=255)
    parent_partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    title = models.CharField(max_length=4, blank=True)
    job_position = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    internal_notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.parent_partner.name} - {self.name}'
