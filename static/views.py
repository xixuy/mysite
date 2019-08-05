from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse
from django.urls import reverse





def forget_pwd(request):

    return render(request, 'forget_pwd.html')


