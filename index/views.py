from django.shortcuts import render

# Create your views here.
from index.models import Artical


def index(request):
    title=Artical.objects.all()
    return render(request,'index.html',{'title':title})


