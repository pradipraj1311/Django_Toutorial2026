from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def secret_page(request):
    # Only logged in users see this
        ...
        
# Create your views here.
