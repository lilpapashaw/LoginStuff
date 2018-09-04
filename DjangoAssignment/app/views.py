"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'app/home.html')

@login_required
def dashboard(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/dashboard.html')