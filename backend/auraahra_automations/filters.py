"""
auraahra_automations/filters.py
"""

from auraahra.filters import auraahraFilterSet, django_filters
from auraahra_automations.models import MailAutomation


class AutomationFilter(auraahraFilterSet):
    """
    AutomationFilter
    """

    search = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = MailAutomation
        fields = "__all__"



