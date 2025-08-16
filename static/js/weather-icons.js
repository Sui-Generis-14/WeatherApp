/**
 * Weather Icons System
 * Maps weather codes to appropriate icons and provides utility functions
 * Created by: Sneha Uppu
 */

const WeatherIcons = {
    // Weather code mappings based on Open-Meteo API
    // https://open-meteo.com/en/docs
    codes: {
        0: { icon: 'fas fa-sun', name: 'Clear Sky', emoji: '☀️', color: '#FFD700' },
        1: { icon: 'fas fa-cloud-sun', name: 'Mainly Clear', emoji: '🌤️', color: '#87CEEB' },
        2: { icon: 'fas fa-cloud-sun', name: 'Partly Cloudy', emoji: '⛅', color: '#B0C4DE' },
        3: { icon: 'fas fa-cloud', name: 'Overcast', emoji: '☁️', color: '#778899' },
        45: { icon: 'fas fa-smog', name: 'Foggy', emoji: '🌫️', color: '#D3D3D3' },
        48: { icon: 'fas fa-smog', name: 'Depositing Rime Fog', emoji: '🌫️', color: '#D3D3D3' },
        51: { icon: 'fas fa-cloud-rain', name: 'Light Drizzle', emoji: '🌦️', color: '#87CEEB' },
        53: { icon: 'fas fa-cloud-rain', name: 'Moderate Drizzle', emoji: '🌧️', color: '#4682B4' },
        55: { icon: 'fas fa-cloud-rain', name: 'Dense Drizzle', emoji: '🌧️', color: '#4682B4' },
        56: { icon: 'fas fa-cloud-rain', name: 'Light Freezing Drizzle', emoji: '🌨️', color: '#B0C4DE' },
        57: { icon: 'fas fa-cloud-rain', name: 'Dense Freezing Drizzle', emoji: '🌨️', color: '#B0C4DE' },
        61: { icon: 'fas fa-cloud-showers-heavy', name: 'Slight Rain', emoji: '🌧️', color: '#4682B4' },
        63: { icon: 'fas fa-cloud-showers-heavy', name: 'Moderate Rain', emoji: '🌧️', color: '#4169E1' },
        65: { icon: 'fas fa-cloud-showers-heavy', name: 'Heavy Rain', emoji: '🌧️', color: '#000080' },
        66: { icon: 'fas fa-cloud-showers-heavy', name: 'Light Freezing Rain', emoji: '🌨️', color: '#B0C4DE' },
        67: { icon: 'fas fa-cloud-showers-heavy', name: 'Heavy Freezing Rain', emoji: '🌨️', color: '#B0C4DE' },
        71: { icon: 'fas fa-snowflake', name: 'Slight Snow', emoji: '❄️', color: '#F0F8FF' },
        73: { icon: 'fas fa-snowflake', name: 'Moderate Snow', emoji: '❄️', color: '#E6E6FA' },
        75: { icon: 'fas fa-snowflake', name: 'Heavy Snow', emoji: '❄️', color: '#FFFFFF' },
        77: { icon: 'fas fa-snowflake', name: 'Snow Grains', emoji: '❄️', color: '#F0F8FF' },
        80: { icon: 'fas fa-cloud-rain', name: 'Slight Rain Showers', emoji: '🌦️', color: '#87CEEB' },
        81: { icon: 'fas fa-cloud-showers-heavy', name: 'Moderate Rain Showers', emoji: '🌧️', color: '#4682B4' },
        82: { icon: 'fas fa-cloud-showers-heavy', name: 'Violent Rain Showers', emoji: '🌧️', color: '#000080' },
        85: { icon: 'fas fa-snowflake', name: 'Slight Snow Showers', emoji: '🌨️', color: '#F0F8FF' },
        86: { icon: 'fas fa-snowflake', name: 'Heavy Snow Showers', emoji: '🌨️', color: '#FFFFFF' },
        95: { icon: 'fas fa-bolt', name: 'Thunderstorm', emoji: '⛈️', color: '#4B0082' },
        96: { icon: 'fas fa-bolt', name: 'Thunderstorm with Slight Hail', emoji: '⛈️', color: '#4B0082' },
        99: { icon: 'fas fa-bolt', name: 'Thunderstorm with Heavy Hail', emoji: '⛈️', color: '#4B0082' }
    },

    // Get weather icon data by code
    getIcon: function(code) {
        return this.codes[code] || this.codes[0]; // Default to clear sky
    },

    // Get icon HTML
    getIconHTML: function(code, size = '2x') {
        const iconData = this.getIcon(code);
        return `<i class="${iconData.icon} fa-${size}" style="color: ${iconData.color};"></i>`;
    },

    // Get emoji
    getEmoji: function(code) {
        return this.getIcon(code).emoji;
    },

    // Get weather name
    getName: function(code) {
        return this.getIcon(code).name;
    },

    // Get color
    getColor: function(code) {
        return this.getIcon(code).color;
    },

    // Create weather card with icon
    createWeatherCard: function(code, temperature, description, location, time) {
        const iconData = this.getIcon(code);
        return `
            <div class="weather-card" style="background: linear-gradient(135deg, ${iconData.color}20, ${iconData.color}40);">
                <div class="weather-icon">
                    ${this.getIconHTML(code, '3x')}
                </div>
                <div class="weather-info">
                    <h3>${temperature}°C</h3>
                    <p class="weather-description">${description}</p>
                    <p class="weather-location">${location}</p>
                    <p class="weather-time">${time}</p>
                </div>
            </div>
        `;
    },

    // Update weather display with icons
    updateWeatherDisplay: function(weatherData) {
        const currentWeather = weatherData.current;
        const forecast = weatherData.forecast;
        
        // Update current weather
        if (currentWeather) {
            const currentIcon = this.getIconHTML(currentWeather.weather_code, '4x');
            const currentCard = this.createWeatherCard(
                currentWeather.weather_code,
                currentWeather.temperature,
                this.getName(currentWeather.weather_code),
                weatherData.location.name,
                new Date().toLocaleTimeString()
            );
            
            // Update DOM elements
            const iconElement = document.getElementById('current-weather-icon');
            const cardElement = document.getElementById('current-weather-card');
            
            if (iconElement) iconElement.innerHTML = currentIcon;
            if (cardElement) cardElement.innerHTML = currentCard;
        }

        // Update forecast
        if (forecast && forecast.daily) {
            const forecastContainer = document.getElementById('forecast-container');
            if (forecastContainer) {
                let forecastHTML = '<div class="row">';
                
                forecast.daily.time.forEach((date, index) => {
                    if (index < 5) { // 5-day forecast
                        const weatherCode = forecast.daily.weather_code[index];
                        const tempMax = forecast.daily.temperature_2m_max[index];
                        const tempMin = forecast.daily.temperature_2m_min[index];
                        
                        const dayName = new Date(date).toLocaleDateString('en-US', { weekday: 'short' });
                        const iconHTML = this.getIconHTML(weatherCode, '2x');
                        
                        forecastHTML += `
                            <div class="col-md-2 col-sm-4 col-6 mb-3">
                                <div class="forecast-card text-center p-3" style="background: linear-gradient(135deg, ${this.getColor(weatherCode)}20, ${this.getColor(weatherCode)}40);">
                                    <div class="forecast-day">${dayName}</div>
                                    <div class="forecast-icon mb-2">${iconHTML}</div>
                                    <div class="forecast-temp">
                                        <span class="temp-max">${tempMax}°</span>
                                        <span class="temp-min">${tempMin}°</span>
                                    </div>
                                    <div class="forecast-desc">${this.getName(weatherCode)}</div>
                                </div>
                            </div>
                        `;
                    }
                });
                
                forecastHTML += '</div>';
                forecastContainer.innerHTML = forecastHTML;
            }
        }
    }
};

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = WeatherIcons;
}
