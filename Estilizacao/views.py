from django.shortcuts import render

def Landing_Page(request):
    return render(request, 'landing.html')
