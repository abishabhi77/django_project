from django.shortcuts import render

# Create your views here.

def login_page(request):
    return render(request, 'login.html')

def form_page(request):
    return render(request,'form.html')