from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin

class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ['image', 'preview_image',]
    readonly_fields = ('preview_image',)

    def preview_image(self, obj):

        return format_html(f'<img src="/media/{obj.image}" style=max-width:200px; max-height: 200px;/>')


class PlaceAdmin(admin.ModelAdmin):

    inlines = [
        ImageInline
    ]



# Register your models here.
admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)