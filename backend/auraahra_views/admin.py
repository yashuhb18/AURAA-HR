from django.contrib import admin

from auraahra_views.models import ActiveGroup, ActiveTab, SavedFilter, ToggleColumn

admin.site.register([ToggleColumn, ActiveTab, ActiveGroup])


