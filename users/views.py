from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.htm')

def dashboard(request):
    return render(request, 'dashboard.html')