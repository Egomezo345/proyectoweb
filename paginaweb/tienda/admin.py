from django.contrib import admin
from .models import CategoriaProd, Producto
# Register your models here.

class CategoriaProdadmin(admin.ModelAdmin):
    
    readonly_fields = ("created", "updated")
    
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(CategoriaProd, CategoriaProdadmin)

admin.site.register(Producto, ProductoAdmin)