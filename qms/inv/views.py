from django.shortcuts import render

def home(request):
    return render(request, 'inv/home.html')