from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/register/')
def home(response):
    return render(response, "main/home.html", {})