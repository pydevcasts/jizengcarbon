from django.contrib import admin
from . import models
from painless.models.actions import PostableMixin,ExportMixin
from django.utils.html import format_html




@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin, PostableMixin, ExportMixin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50%;">'.format(object.banner_1.url))
    thumbnail.short_description = 'Product Picture'
    list_display = ['thumbnail', 'title', 'slug', 'is_published', 'published','views', 'category', 'get_tags']
    list_editable = ['category']
    list_display_links = ["title"]
    filter_horizontal = ['tags']
    list_filter = ['status', 'published_at', 'category__title']
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']
  
    fieldsets = [
        ('main', { 
            'fields': ( 
                    ('title',), 
                    ('author', 'status', ),
                    ('category','views'),
                ),
            }
        ),

        ('Advanced_options', { 
            'fields': (
                    'tags',
                    'banner_1',
                    'banner_2',
                    'banner_3',
                    'summary',
                    'content',
                    'published_at',
                ),
            'classes': ('collapse',)
            },

        ),
    ]



    def get_tags(self, obj):
        return ", ".join([t.title for t in obj.tags.all()])

    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('published_at',)
        return []


