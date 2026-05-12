"""
auraahra Branding Context Processor

This module provides branding and configuration context to all templates
"""

from django.conf import settings


def auraahra_branding(request):
    """
    Context processor to inject auraahra branding throughout the application
    """
    branding = getattr(settings, 'AURAAHRA_BRANDING', {
        "APP_NAME": "auraahra",
        "TAGLINE": "Unified Workforce Intelligence Platform",
        "DESCRIPTION": "Enterprise AI-powered workforce management platform",
        "VERSION": "2.0.0",
        "PRIMARY_COLOR": "#5b81ff",
        "SECONDARY_COLOR": "#a855f7",
        "ACCENT_CYAN": "#06b6d4",
        "ACCENT_EMERALD": "#10b981",
    })
    
    return {
        'auraahra': branding,
        'app_name': branding.get('APP_NAME', 'auraahra'),
        'tagline': branding.get('TAGLINE', 'Unified Workforce Intelligence Platform'),
        'version': branding.get('VERSION', '2.0.0'),
    }

