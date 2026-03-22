from django.contrib import admin
from .models import TelegramUser, AccessRequest

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'username', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('telegram_id', 'username')
    
@admin.register(AccessRequest)
class AccessRequestAdmin(admin.ModelAdmin):
    list_display = ('telegram_user', 'service_name', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('service_name', 'telegram_user__username')
    actions = ['approve_requests', 'reject_requests']
    
    def approve_requests(self, request, queryset):
        queryset.update(status='approved')
    approve_requests.short_description = "Одобрить выбранные запросы"
    
    def reject_requests(self, request, queryset):
        queryset.update(status='rejected')
    reject_requests.short_description = "Отказать в выбранных запросах"
    
