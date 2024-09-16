from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'about/index.html')

def services(request):
    return render(request, 'services/index.html')