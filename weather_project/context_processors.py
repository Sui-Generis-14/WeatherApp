from django.conf import settings

def settings_context(request):
    return {
        'settings': {
            'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
        }
    }


