from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'super/home.html', context={'scss_filename': 'home.scss'})
