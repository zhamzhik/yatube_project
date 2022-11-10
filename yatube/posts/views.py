from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse(f'Группа {slug}')


# В урл мы ждем параметр, и нужно его прередать в функцию для использования
