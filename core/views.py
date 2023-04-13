from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def contract(request):
    return render(request, 'core/contract.html')