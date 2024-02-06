from django.contrib import admin
from .models import BMW

# Register your models here.
# admin.site.register(BMW)

@admin.register(BMW)
class AdminOnlineShop(admin.ModelAdmin):
    list_display=['price', 'name', 'islike', 'image_tag']
    readonly_fields = ['image_tag']