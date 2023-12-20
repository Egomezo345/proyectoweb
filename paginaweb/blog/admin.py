from django.contrib import admin
from .models import categoria, post
# Register your models here.

class categoriaadmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

class postadmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(categoria, categoriaadmin)
admin.site.register(post, postadmin)