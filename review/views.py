from django.shortcuts import render

def index(request):
    return render(request, 'review/index.html', {})
# Create your views here.
