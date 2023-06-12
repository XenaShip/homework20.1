from django.contrib import admin
from homework.models import Product, Category
# Register your models here.

'''
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name',)
'''


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_product', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name_product', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_category')
    list_filter = ('name_category',)
    search_fields = ('name_category', 'description',)
