from django.contrib import admin
from .models import Product, Category, Package
from tabbed_admin import TabbedModelAdmin


class PackageInline(admin.StackedInline):
    model = Package
    extra = 0

class ProductAdmin(TabbedModelAdmin):
    list_display = ('internal_reference', 'name',)
    tab_informations = (
        (None, {
            'fields': (
                ('image', 'name'),
                ('internal_reference', 'can_be_sold'),
                'category',
                'barcode',
                'description',
            ),
        }),
    )
    tab_sales = (
        (None, {
            'fields': (
                ('price', 'cost'),
                'minimum_sale_qty'
            ),
        }),
    )
    tab_inventory = (
        (None, {
            'fields': (
                ('weight', 'volume'),
            ),
        }),
        PackageInline,
    )
    tabs = [
        ('General informations', tab_informations),
        ('Sales informations', tab_sales),
        ('Inventory informations', tab_inventory),
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
