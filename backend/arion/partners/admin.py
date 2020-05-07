from django.contrib import admin
from .models import Partner, Contact

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

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('internal_code', 'name',)
    inlines = (ContactInline,)
    fieldsets = (
        (None, {
            'fields': ('logo', 'name', ('internal_code', 'company_number'), 'website', 'hq_address'),
        }),
        (None, {
            'fields': ('internal_notes',)
        }),
    )


admin.site.register(Partner, PartnerAdmin)
admin.site.register(Contact, ContactAdmin)
