from django.contrib import admin
from django.utils.safestring import mark_safe
from restaurant_app.models import MenuItem

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):

    # отображение изображений блюд в админке
    @admin.display(description="Изображение")
    def post_photo(self, photo: MenuItem):
        if photo.image:
            return mark_safe(f"<img src='{photo.image.url}' width=50>")
        return "Без фото"

    list_display = ['post_photo', 'type', 'title', 'description', 'price']
    ordering = ['type']
    readonly_fields = ['post_photo']

admin.site.register(MenuItem, MenuItemAdmin)