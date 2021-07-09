from django.shortcuts import render


def home(request):
    return render(request, 'super/home.html', context={
        'scss_path': 'super/style/home.scss', 
        'ts_path': 'super/script/home.ts'
    })
