from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta
from .models import WeatherRecord

class WeatherRecordForm(forms.ModelForm):
    """Form for creating and editing weather records"""
    
    class Meta:
        model = WeatherRecord
        fields = [
            'location_name', 'location_type', 'latitude', 'longitude',
            'start_date', 'end_date', 'temperature_min', 'temperature_max',
            'temperature_avg', 'humidity', 'pressure', 'wind_speed',
            'wind_direction', 'description', 'icon', 'precipitation',
            'visibility', 'uv_index', 'notes'
        ]
        widgets = {
            'location_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter location name (e.g., New York, NY)'
            }),
            'location_type': forms.Select(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.000001',
                'placeholder': 'e.g., 40.7128'
            }),
            'longitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.000001',
                'placeholder': 'e.g., -74.0060'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'temperature_min': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Minimum temperature in Celsius'
            }),
            'temperature_max': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Maximum temperature in Celsius'
            }),
            'temperature_avg': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Average temperature in Celsius'
            }),
            'humidity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'max': '100',
                'placeholder': 'Humidity percentage (0-100)'
            }),
            'pressure': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Atmospheric pressure in hPa'
            }),
            'wind_speed': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Wind speed in m/s'
            }),
            'wind_direction': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., N, NE, E, SE, S, SW, W, NW'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Weather description (e.g., Clear sky, Rain)'
            }),
            'icon': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Weather icon code (e.g., 01d, 10n)'
            }),
            'precipitation': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Precipitation in mm'
            }),
            'visibility': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Visibility in km'
            }),
            'uv_index': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1',
                'placeholder': 'UV index (0-11)'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Additional notes about this weather record'
            }),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        temperature_min = cleaned_data.get('temperature_min')
        temperature_max = cleaned_data.get('temperature_max')
        latitude = cleaned_data.get('latitude')
        longitude = cleaned_data.get('longitude')
        
        # Validate date range
        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError("Start date cannot be after end date")
            
            # Check if date range is not more than 30 days
            date_diff = (end_date - start_date).days
            if date_diff > 30:
                raise ValidationError("Date range cannot exceed 30 days")
            
            # Check if dates are not in the future
            today = timezone.now().date()
            if start_date > today or end_date > today:
                raise ValidationError("Dates cannot be in the future")
        
        # Validate temperature range
        if temperature_min is not None and temperature_max is not None:
            if temperature_min > temperature_max:
                raise ValidationError("Minimum temperature cannot be higher than maximum temperature")
        
        # Validate coordinates
        if latitude is not None:
            if not -90 <= latitude <= 90:
                raise ValidationError("Latitude must be between -90 and 90 degrees")
        
        if longitude is not None:
            if not -180 <= longitude <= 180:
                raise ValidationError("Longitude must be between -180 and 180 degrees")
        
        return cleaned_data
    
    def clean_humidity(self):
        humidity = self.cleaned_data.get('humidity')
        if humidity is not None and (humidity < 0 or humidity > 100):
            raise ValidationError("Humidity must be between 0 and 100 percent")
        return humidity
    
    def clean_uv_index(self):
        uv_index = self.cleaned_data.get('uv_index')
        if uv_index is not None and (uv_index < 0 or uv_index > 11):
            raise ValidationError("UV index must be between 0 and 11")
        return uv_index

class WeatherSearchForm(forms.Form):
    """Form for searching weather data"""
    
    LOCATION_TYPES = [
        ('city', 'City'),
        ('zip', 'Zip Code'),
        ('coordinates', 'GPS Coordinates'),
        ('landmark', 'Landmark'),
    ]
    
    location = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter city, zip code, coordinates, or landmark...'
        })
    )
    
    location_type = forms.ChoiceField(
        choices=LOCATION_TYPES,
        initial='city',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    def clean_location(self):
        location = self.cleaned_data.get('location')
        if not location or len(location.strip()) == 0:
            raise ValidationError("Location is required")
        return location.strip()



