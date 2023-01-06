from django.contrib import admin
from . import models
from django.utils.html import format_html
from painless.models.actions import PostableMixin,ExportMixin



@admin.register(models.CustomerFeedback)
class CustomeFeedbackAdmin(admin.ModelAdmin, PostableMixin, ExportMixin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50%;">'.format(object.banner.url))
    thumbnail.short_description = 'TestMonials picture'
    list_display = ['thumbnail','first_name','last_name','is_published','status', 'published','role']
    list_filter = ['status', 'published_at',]
    list_display_links = ['first_name']
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']
  
    fieldsets = [
        ('main', { 
            'fields': ( 
                    ('first_name','last_name'), 
                    ('role', 'status', 'banner'),
                    ('content'),
                ),
            }
        ),

      
    ]

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('published_at',)
        return []

