from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery, SizeColorStock
# ติดตั้ง pip install django-admin-thumbnails ก่อน import admin_thumbnails
import admin_thumbnails  # ใช้โชว์รูปภาพ สินค้าในส่วนของ หน้าadmin


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available', 'images')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category','variation_value', 'is_active')
    list_editable = ('variation_value', 'is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')


# class SizeColorStockAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('size',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
admin.site.register(SizeColorStock)
