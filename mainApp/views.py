from django.shortcuts import render

def mainApp(request):
    return render(request, 'mainApp/index.html')
