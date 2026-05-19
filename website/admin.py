from django.contrib import admin
from .models import PageContent, Service, ContactMessage

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title')
    search_fields = ('title', 'content')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    
    # Make contact messages mostly read-only in the admin panel to prevent accidental edits
    def has_add_permission(self, request):
        return False
