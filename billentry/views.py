from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from billentry.models import Payment, Receipt

@login_required
def index(request):
    return render(request, 'billentry/index.html', 
                  {'user_full_name' : request.user.get_full_name()}, 
                  content_type = 'text/html')


