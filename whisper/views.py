from django.shortcuts import render

# Create your views here.


def whisper(request):
    return render(request,'whisper.html')
