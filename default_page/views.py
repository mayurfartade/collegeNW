from django.shortcuts import render

# Create your views here.

def default(request):
    return render(request, 'default_page/default.html')