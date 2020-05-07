from django.contrib import admin
from .models import Partner, Contact
from tabbed_admin import TabbedModelAdmin

contact_fieldsets = (
    (None, {
        'fields': (
            ('title', 'name', 'job_position'),
            ('email', 'phone_number', 'mobile_number'),
            'internal_notes'
        ),
    }),
)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('parent_partner', 'name', 'job_position',)
    fieldsets = ((None, {'fields': ('parent_partner',)}), contact_fieldsets[0])

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 0
    fieldsets = contact_fieldsets

class PartnerAdmin(TabbedModelAdmin):
    list_display = ('internal_code', 'name',)
    tab_informations = (
        (None, {
            'fields': ('logo', 'name', ('internal_code', 'company_number'), 'website', 'address'),
        }),
    )
    tab_contacts = (
        ContactInline,
    )
    tab_internal_notes = (
        (None, {
            'fields': ('internal_notes',)
        }),
    )
    tabs = [
        ('Informations', tab_informations),
        ('Contacts', tab_contacts),
        ('Internal Notes', tab_internal_notes),
    ]


admin.site.register(Partner, PartnerAdmin)
admin.site.register(Contact, ContactAdmin)
