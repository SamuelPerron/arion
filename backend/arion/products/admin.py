from django.contrib import admin
from .models import Product, Category
from tabbed_admin import TabbedModelAdmin


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
            ),
        }),
    )
    tab_inventory = (
        (None, {
            'fields': (
                ('weight', 'volume'),
            ),
        }),
    )
    tabs = [
        ('General informations', tab_informations),
        ('Sales informations', tab_sales),
        ('Inventory informations', tab_inventory),
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
