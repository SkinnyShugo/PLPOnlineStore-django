from django.contrib import admin
from .models import Product, Order, OrderItem
from category.models import Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 5

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product', {'fields': ['product'],}),
        ('Quantity', {'fields': ['quantity'],}),
        ('Price', {'fields': ['price'],}),
    ]
    readonly_fields = ('product', 'quantity', 'price')
    can_delete = False
    max_num = 0

# Register your models here.
admin.site.register(Product, ProductAdmin)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billingName', 'emailAddress', 'created']
    list_display_links = ('id', 'billingName')
    search_fields = ['id', 'billingName', 'emailAddress']
    readonly_fields = ['id', 'token', 'total', 'emailAddress', 'created', 'billingName', 'billingAddress1', 'billingCity', 'billingPostalCode', 'billingCountry', 'shippingName', 'shippingAddress1', 'shippingCity', 'shippingPostalCode', 'shippingCountry']
    fieldsets = [
        ('ORDER INFORMATION', {'fields': ['id', 'token', 'total', 'created']}),
        ('BILLING INFORMATION', {'fields': ['emailAddress','billingName', 'billingAddress1', 'billingCity', 'billingPostalCode', 'billingCountry']}),
        ('SHIPPING INFORMATION', {'fields': ['shippingName', 'shippingAddress1', 'shippingCity', 'shippingPostalCode', 'shippingCountry']}),
    ]

    inlines = [
        OrderItemAdmin,
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False