from django.db import models

class Address(models.Model):
    line1 = models.CharField(max_length=255, verbose_name='Line 1')
    line2 = models.CharField(max_length=255, verbose_name='Line 2', blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.line1} {self.line2}, {self.city} {self.state}, {self.country}'

    class Meta:
        verbose_name_plural = 'Addresses'
