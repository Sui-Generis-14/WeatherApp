from django.contrib import admin
from .models import WeatherRecord, WeatherSearch

@admin.register(WeatherRecord)
class WeatherRecordAdmin(admin.ModelAdmin):
    list_display = [
        'location_name', 'location_type', 'start_date', 'end_date', 
        'temperature_min', 'temperature_max', 'temperature_avg', 
        'humidity', 'created_at'
    ]
    list_filter = [
        'location_type', 'start_date', 'end_date', 'created_at', 
        'updated_at'
    ]
    search_fields = [
        'location_name', 'description', 'notes'
    ]
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Location Information', {
            'fields': ('location_name', 'location_type', 'latitude', 'longitude')
        }),
        ('Date Range', {
            'fields': ('start_date', 'end_date')
        }),
        ('Weather Data', {
            'fields': (
                'temperature_min', 'temperature_max', 'temperature_avg',
                'humidity', 'pressure', 'wind_speed', 'wind_direction',
                'description', 'icon'
            )
        }),
        ('Additional Data', {
            'fields': ('precipitation', 'visibility', 'uv_index'),
            'classes': ('collapse',)
        }),
        ('Metadata', {
            'fields': ('notes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_duration_days(self, obj):
        return obj.get_duration_days()
    get_duration_days.short_description = 'Duration (Days)'
    
    def get_temperature_range(self, obj):
        return obj.get_temperature_range()
    get_temperature_range.short_description = 'Temperature Range'

@admin.register(WeatherSearch)
class WeatherSearchAdmin(admin.ModelAdmin):
    list_display = [
        'location_query', 'search_type', 'success', 'timestamp'
    ]
    list_filter = [
        'search_type', 'success', 'timestamp'
    ]
    search_fields = ['location_query', 'error_message']
    readonly_fields = ['timestamp']
    date_hierarchy = 'timestamp'
    ordering = ['-timestamp']
    
    def has_add_permission(self, request):
        return False  # Weather searches are created automatically
    
    def has_change_permission(self, request, obj=None):
        return False  # Weather searches should not be edited
    
    def has_delete_permission(self, request, obj=None):
        return True  # Allow deletion for cleanup
