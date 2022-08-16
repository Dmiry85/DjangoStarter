from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def bio(request, username):
    print(username)
    return render(request, 'index.html')


def article_case_2023(request):
    print(request)
    return HttpResponse('Special_case_2023')


def year_archive(request, year):
    print(request)
    print(year)
    if year == 2003:
        return HttpResponse('Special_case_2003')
    return HttpResponse(f'{year}')
