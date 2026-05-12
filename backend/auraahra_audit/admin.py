"""
admin.py
"""

from django.contrib import admin

from auraahra_audit.models import AuditTag, auraahraAuditInfo, auraahraAuditLog

# Register your models here.

admin.site.register(AuditTag)


