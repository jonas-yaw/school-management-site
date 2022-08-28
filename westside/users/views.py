#from random import random
#from urllib import request
#from django.shortcuts import render
#from django.contrib.sites.shortcuts import get_current_site
#from django.conf import settings
#from django.core.mail import send_mail
#from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
