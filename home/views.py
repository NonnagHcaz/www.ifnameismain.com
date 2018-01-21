from django.shortcuts import render
from .models import Author, Theme

import json

try:
    from kharon import kharon
    kharon_avail = True
except Exception:
    kharon_avail = False

# from django.http import HttpResponse
THEMES = [
    {
        "author": ["Gannon"],
        "name": "Carbon Gold",
        "id": "carbon_gold",
        "primary": "gold",
        "secondary": "#343434",
        "tags": []
    },
    {
        "author": ["Gannon"],
        "name": "Doctor Doom",
        "id": "doom",
        "primary": "silver",
        "secondary": "darkgreen",
        "tags": ["comics", "marvel", "fantastic 4", "anti-hero"]
    },
    {
        "author": ["Gannon"],
        "name": "Galactus",
        "id": "galactus",
        "primary": "slateblue",
        "secondary": "darkmagenta",
        "tags": ["comics", "marvel", "x-men", "anti-hero"]
    },
    {
        "author": ["Gannon"],
        "name": "Hotline Miami",
        "id": "hotline_miami",
        "primary": "aqua",
        "secondary": "purple",
        "tags": ["games", "hotline miami"]
    },
    {
        "author": ["Gannon"],
        "name": "Hulk",
        "id": "hulk",
        "primary": "green",
        "secondary": "purple",
        "tags": ["comics", "marvel", "avengers", "hero"]
    },
    {
        "author": ["Gannon"],
        "name": "Iron Man",
        "id": "iron_man",
        "primary": "#beba46",
        "secondary": "#771414",
        "tags": ["comics", "marvel", "avengers", "hero"]
    },
    {
        "author": ["Gannon"],
        "name": "Loki",
        "id": "loki",
        "primary": "goldenrod",
        "secondary": "darkolivegreen",
        "tags": ["comics", "marvel", "avengers", "anti-hero"]
    },
    {
        "author": ["Gannon"],
        "name": "Lucio",
        "id": "lucio",
        "primary": "yellow",
        "secondary": "green",
        "tags": ["games", "overwatch"]
    },
    {
        "author": ["Gannon"],
        "name": "Magneto",
        "id": "magneto",
        "primary": "#c70039",
        "secondary": "#581845",
        "tags": ["comics", "marvel", "x-men", "anti-hero"]
    },
    {
        "author": ["Gannon"],
        "name": "Matrix",
        "id": "matrix",
        "primary": "green",
        "secondary": "black",
        "tags": ["movies", "the matrix"]
    },
    {
        "author": ["Gannon"],
        "name": "Thanos",
        "id": "thanos",
        "primary": "gold",
        "secondary": "#1a43d4",
        "tags": ["comics", "marvel", "infinity saga", "anti-hero"]
    }
]


def themes_view(request):
    # Theme.objects.all().delete()
    # for theme in THEMES:
    #     new_theme = Theme(
    #         key=theme['id'],
    #         name=theme['name'],
    #         primary=theme['primary'],
    #         secondary=theme['secondary'])
    #     new_theme.save()
    # themes = Theme.objects.all()
    # print('\n' + '*' * 72 + '\n')
    # for theme in themes:
    #     print(str(theme))
    # print('\n' + '*' * 72 + '\n')
    return render(request, 'themes.html')


def about_view(request):
    return render(request, 'about.html')


def cookies_view(request):
    return render(request, 'cookies.html')


def home_view(request):
    return render(request, 'home.html')


def wip_view(request):
    return render(request, 'wip.html')


def gaming_view(request):
    return render(request, 'gaming.html')


def music_view(request):
    return render(request, 'music.html')


def contact_view(request):
    return render(request, 'contact.html')


def coding_view(request):
    return render(request, 'coding.html')


def wd2_view(request):
    return render(request, 'wd2.html')


def landing_view(request):
    if 'landed' in request.COOKIES or request.user_agent.is_touch_capable:
        response = home_view(request)
    elif not request.user_agent.is_touch_capable:
        response = wd2_view(request)
        response.set_cookie('landed', '1')
    return response


def submit_view(request):
    return render(request, 'submit.html')


def kharon_view(request):
    preview = ''
    output = ''
    target = 'content'

    username = request.GET.get('username_text') or 'gannon93'
    reponame = request.GET.get('reponame_text') or 'gkit_cogs'
    cogname = request.GET.get('cogname_text') or 'basta'

    if request.GET.get('upload_github_button'):
        if kharon_avail:
            try:
                preview = json.dumps(
                    kharon.get_info(
                        username.lower(), reponame.lower(), cogname.lower()),
                    sort_keys=True)
                target = 'convert'
            except Exception as e:
                pass
    elif request.GET.get('convert_button'):
        data = request.GET.get('upload_preview_textarea')
        preview = json.loads(data)
        if kharon_avail:
            output = kharon.format_info(preview)
        target = 'export'
    return render(
        request, 'kharon.html', {
            'preview': preview,
            'output': output,
            'username': username,
            'reponame': reponame,
            'cogname': cogname,
            'gotodiv': target})
