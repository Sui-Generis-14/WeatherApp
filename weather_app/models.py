from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, timedelta

class WeatherRecord(models.Model):
    """Model to store weather data with location and date range"""
    
    LOCATION_TYPES = [
        ('city', 'City'),
        ('zip', 'Zip Code'),
        ('coordinates', 'GPS Coordinates'),
        ('landmark', 'Landmark'),
    ]
    
    # Location information
    location_name = models.CharField(max_length=200, help_text="Name of the location")
    location_type = models.CharField(max_length=20, choices=LOCATION_TYPES, default='city')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    # Date range
    start_date = models.DateField(help_text="Start date for weather data")
    end_date = models.DateField(help_text="End date for weather data")
    
    # Weather data
    temperature_min = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    temperature_max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    temperature_avg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    humidity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=True, blank=True
    )
    pressure = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    wind_direction = models.CharField(max_length=10, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    icon = models.CharField(max_length=50, null=True, blank=True)
    
    # Additional data
    precipitation = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    visibility = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    uv_index = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True, help_text="Additional notes about this weather record")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Weather Record"
        verbose_name_plural = "Weather Records"
    
    def __str__(self):
        return f"{self.location_name} ({self.start_date} to {self.end_date})"
    
    def clean(self):
        """Validate the model data"""
        from django.core.exceptions import ValidationError
        
        # Validate date range
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError("Start date cannot be after end date")
            
            # Check if date range is not more than 30 days
            date_diff = (self.end_date - self.start_date).days
            if date_diff > 30:
                raise ValidationError("Date range cannot exceed 30 days")
        
        # Validate coordinates if provided
        if self.latitude is not None:
            try:
                lat_val = float(self.latitude)
                if not -90 <= lat_val <= 90:
                    raise ValidationError("Latitude must be between -90 and 90")
            except (ValueError, TypeError):
                raise ValidationError("Invalid latitude value")
        
        if self.longitude is not None:
            try:
                lon_val = float(self.longitude)
                if not -180 <= lon_val <= 180:
                    raise ValidationError("Longitude must be between -180 and 180")
            except (ValueError, TypeError):
                raise ValidationError("Invalid longitude value")
    
    def get_temperature_range(self):
        """Get formatted temperature range"""
        if self.temperature_min and self.temperature_max:
            return f"{self.temperature_min}°C - {self.temperature_max}°C"
        elif self.temperature_avg:
            return f"{self.temperature_avg}°C"
        return "N/A"
    
    def get_duration_days(self):
        """Get the number of days in the date range"""
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date).days + 1
        return 0

class WeatherSearch(models.Model):
    """Model to track weather searches for analytics"""
    
    location_query = models.CharField(max_length=200)
    search_type = models.CharField(max_length=20, choices=[
        ('current', 'Current Weather'),
        ('forecast', 'Forecast'),
        ('historical', 'Historical'),
    ])
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=True)
    error_message = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.location_query} - {self.search_type} ({self.timestamp})"
