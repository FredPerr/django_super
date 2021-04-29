from django.shortcuts import render

def home(request):
    return render(request, 'super/home.html', context={'scss_filename': 'home.scss', 'script_filename': 'home.ts'})
