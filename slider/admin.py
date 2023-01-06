from django.contrib import admin
from slider.models import  Slider
from painless.models.actions import PostableMixin,ExportMixin
from django.utils.html import format_html

  

 

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin, PostableMixin, ExportMixin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50%;">'.format(object.banner.url))
    thumbnail.short_description = 'Product Picture'
    list_display = ['thumbnail','title', 'status', 'is_published', 'published']
    list_filter = ['status', 'published_at']
    list_display_links = ['title']
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']
  
    fieldsets = [
        ('main', { 
            'fields': ( 
                    ('title','summary',), 
                    ('banner'),
                    ('status'),
                    ('content')
                ),
            }
        ),

    ]

    search_fields = ('title',)
    ordering = ('title',)

    def published(self, obj):
        return (obj.published_at)


    def is_published(self, obj):
        published = 1
        return obj.status == published
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('published_at',)
        return []

    is_published.boolean = True


