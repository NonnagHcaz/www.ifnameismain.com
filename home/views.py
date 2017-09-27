from django.shortcuts import render
# from django.http import HttpResponse


def home_page(request):
    return render(request, 'home.html')


def wip_page(request):
    return render(request, 'wip.html')


def gaming_page(request):
    return render(request, 'gaming.html')


def music_page(request):
    return render(request, 'music.html')


def contact_page(request):
    return render(request, 'contact.html')


def coding_page(request):
    return render(request, 'coding.html')
