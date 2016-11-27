from django.contrib import admin

from products.models import Product, Category, Producer


class ProducerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Producer, ProducerAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

