from django.contrib import admin
from django.utils.html import format_html

from .models import Auction, AuctionImage

class AuctionImageInline(admin.TabularInline):
    model = AuctionImage
    extra = 5
    fields = ('image',)
    readonly_fields = ('thumbnail',)
    max_num = 5

    def thumbnail(self, instance):
        return format_html('<img src="{}" width="50" height="50" />', instance.image.url)

class AuctionAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'date', 'is_completed')
    list_filter = ('is_completed', 'date' ) 
    search_fields = ('title', 'description')
    ordering = ('-date',)
    inlines = [AuctionImageInline]
    fieldsets = ( 
        (None, {
            'fields': ('title', 'description', 'price', 'date', 'is_completed')
        }),
    )

admin.site.register(Auction, AuctionAdmin)