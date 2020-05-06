from django.db import models

class Partner(models.Model):
    logo = models.ImageField(upload_to='uploads/partner/logos/', blank=True)
    name = models.CharField(max_length=255)
    internal_code = models.CharField(max_length=64, blank=True)
    company_number = models.CharField(max_length=8, blank=True)
    website = models.CharField(max_length=255, blank=True)

    line1 = models.CharField(max_length=255, verbose_name='Line 1')
    line2 = models.CharField(max_length=255, verbose_name='Line 2', blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        if self.internal_code:
            code = f'[{self.internal_code}] '
        else:
            code = ''
        return f'{code}{self.name}'
