from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product, Pages, Articles, Orders

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_show', 'price', 'available', 'created', 'upload']
    list_filter = ['category', 'available', 'created', 'upload']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


    search_fields = ['name', 'slug', 'price',]
    
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Картинка"


# @admin.register(Status)
# class StatusAdmin(admin.ModelAdmin):
#     list_display = ['orderstatus']
#     # prepopulated_fields = {'slug': ('orderstatus',)}
#     search_fields = ['orderstatus']
#     list_filter = ['orderstatus']

# @admin.register(Delivery)
# class DeliveryAdmin(admin.ModelAdmin):
#     list_display = ['delivery']
#     # prepopulated_fields = {'slug': ('delivery',)}
#     search_fields = ['delivery']
#     list_filter = ['delivery']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['person', 'email', 'adress', 'delivery', 'date', 'time', 'comment']
    list_filter = ['person', 'email', 'date', 'time']
    # prepopulated_fields = {'slug': ('status',)}
    list_display_links = None
    search_fields = ['person', 'email', 'date', 'time']
    
    


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name']
    search_fields = ['name',]

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['pages', 'title', 'slug', 'created', 'upload']
    list_filter = ['pages', 'title', 'created', 'upload']
   
    prepopulated_fields = {'slug': ('title',)}


    search_fields = ['pages__name', 'title',]