# Weather App - Technical Assessment

**Created by: Sneha Uppu**

A comprehensive weather application built with Django and modern web technologies, featuring real-time weather data, 5-day forecasts, and advanced CRUD operations with data persistence.

## 🌟 Features

### Tech Assessment 1 (Basic)
- **Location Search**: Enter any location (Zip Code, GPS Coordinates, Landmarks, Town, City)
- **Current Weather**: Real-time weather data with detailed information
- **5-Day Forecast**: Extended weather predictions
- **GPS Location**: Get weather for your current location
- **Weather Icons**: Beautiful weather condition icons
- **Responsive Design**: Works on all devices

### Tech Assessment 2 (Advanced)
- **CRUD Operations**: Create, Read, Update, Delete weather records
- **Data Persistence**: SQLite database with comprehensive weather data storage
- **Date Range Validation**: Validate location and date ranges
- **Data Export**: Export to JSON, CSV, PDF, Excel, and Markdown formats
- **Search & Pagination**: Advanced data management features
- **Real API Integration**: Google Maps Geocoding + Open-Meteo Weather APIs

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone and setup**
   ```bash
   git clone <your-repo-url>
   cd weather-app
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure environment**
   ```bash
   # Copy the example environment file and add your API keys
   cp .env.example .env
   # Edit .env and add your Google Maps API key
   # Required: GOOGLE_MAPS_API_KEY
   ```

3. **Setup database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run application**
   ```bash
   python manage.py runserver
   ```

5. **Access the app**
   - Main app: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 🔧 Configuration

### Required API Keys
- **Google Maps API Key**: Enable Geocoding API and Maps JavaScript API

### Environment Variables
```env
SECRET_KEY=your_django_secret_key
DEBUG=True
GOOGLE_MAPS_API_KEY=Enter your API key here
```

## 🛠️ Technologies

**Backend**: Django 4.2.7, Django REST Framework, SQLite, python-decouple, requests
**Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5, Font Awesome
**APIs**: Open-Meteo API (free weather data), Google Maps Geocoding API
**Export**: JSON, CSV, PDF, Excel, Markdown

## 📝 License

Technical assessment project created by **Sneha Uppu** for PM Accelerator.
