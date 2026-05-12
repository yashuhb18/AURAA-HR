from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path, re_path

import notifications.urls

from . import settings
from base import auraahra_views


def health_check(request):
    return JsonResponse({"status": "ok"}, status=200)


urlpatterns = [
    path("", auraahra_views.modern_dashboard, name="dashboard"),
    path("dashboard/", auraahra_views.modern_dashboard, name="modern_dashboard"),
    path("home/", auraahra_views.modern_dashboard, name="home"),
    path("auth/login/", auraahra_views.modern_login, name="modern_login"),
    path("auth/logout/", auraahra_views.modern_logout, name="modern_logout"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("base.urls")),
    path("", include("auraahra_automations.urls")),
    path("", include("auraahra_views.urls")),
    path("employee/", include("employee.urls")),
    path("auraahra-widget/", include("auraahra_widgets.urls")),
    path("api/", include("auraahra_api.urls")),
    path("recruitment/", include("recruitment.urls")),
    path("attendance/", include("attendance.urls")),
    path("leave/", include("leave.urls")),
    path("payroll/", include("payroll.urls.urls")),
    path("pms/", include("pms.urls")),
    path("asset/", include("asset.urls")),
    path("onboarding/", include("onboarding.urls")),
    path("project/", include("project.urls")),
    path("helpdesk/", include("helpdesk.urls")),
    path("offboarding/", include("offboarding.urls")),
    path("report/", include("report.urls")),
    path("backup/", include("auraahra_backup.urls")),
    re_path(
        "^inbox/notifications/", include(notifications.urls, namespace="notifications")
    ),
    path("i18n/", include("django.conf.urls.i18n")),
    path("health/", health_check),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
