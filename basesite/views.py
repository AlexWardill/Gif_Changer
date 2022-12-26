from django.shortcuts import render

def home(request):
    return render(request, 'basesite/home.html')

def display_gif(request):
  return render(request, 'basesite/display_gif.html')