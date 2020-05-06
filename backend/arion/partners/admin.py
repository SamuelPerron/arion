from django.contrib import admin
from .models import Partner


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('internal_code', 'name', 'country')
    fieldsets = (
        (None, {
            'fields': ('logo', 'name', ('internal_code', 'company_number'), 'website')
        }),
        ('Headquarters', {
            'fields': (('line1', 'line2', 'zip'), ('city', 'state', 'country'))
        }),
    )

admin.site.register(Partner, PartnerAdmin)
