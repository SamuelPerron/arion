from django.contrib import admin
from .models import Address

class AddressAdmin(admin.ModelAdmin):
    list_display = ('line1', 'city', 'state', 'country')
    fieldsets = (
        (None, {
            'fields': (('line1', 'line2', 'zip'), ('city', 'state', 'country')),
        }),
    )


admin.site.register(Address, AddressAdmin)
