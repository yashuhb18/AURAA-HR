"""
auraahra Modern Views

This module contains view handlers for the modern auraahra interface
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


def landing_page(request):
    """
    Render the modern auraahra landing page
    """
    context = {
        'app_name': settings.AURAAHRA_BRANDING.get('APP_NAME', 'auraahra'),
        'tagline': settings.AURAAHRA_BRANDING.get('TAGLINE', 'Unified Workforce Intelligence Platform'),
    }
    return render(request, 'landing_modern.html', context)


def modern_login(request):
    """
    Render the modern login page
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Return login page with error message
            context = {
                'error': 'Invalid username or password',
                'app_name': settings.AURAAHRA_BRANDING.get('APP_NAME', 'auraahra'),
            }
            return render(request, 'login_modern.html', context, status=401)
    
    context = {
        'app_name': settings.AURAAHRA_BRANDING.get('APP_NAME', 'auraahra'),
    }
    return render(request, 'login_modern.html', context)


# @login_required(login_url='modern_login')
def modern_dashboard(request):
    """
    Render the modern dashboard
    """
    from employee.models import Employee
    from recruitment.models import Recruitment
    from leave.models import LeaveRequest
    
    # Get real statistics for the dashboard
    try:
        total_employees = Employee.objects.all().count()
        active_employees = Employee.objects.filter(is_active=True).count()
        open_positions = Recruitment.objects.filter(is_active=True).count()
        # Mocking attrition for now as it's complex, but using a semi-realistic calculation if possible
        attrition_rate = "7.4" 
    except Exception as e:
        print(f"Error calculating stats: {e}")
        total_employees = 0
        active_employees = 0
        open_positions = 0
        attrition_rate = "0"
    
    context = {
        'app_name': settings.AURAAHRA_BRANDING.get('APP_NAME', 'AuraaHR AI'),
        'user': request.user,
        'total_employees': total_employees,
        'active_employees': active_employees,
        'open_positions': open_positions,
        'attrition_rate': attrition_rate,
    }
    return render(request, 'dashboard_modern.html', context)


def modern_logout(request):
    """
    Handle logout and redirect to landing page
    """
    logout(request)
    return redirect('landing_page')

