from django.shortcuts import render
from .models import Author, Theme

import json

try:
    from kharon import kharon
    kharon_avail = True
except Exception:
    kharon_avail = False

# from django.http import HttpResponse


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
    return _render(request, 'themes.html')


def about_view(request):
    return _render(request, 'about.html')


def cookies_view(request):
    return _render(request, 'cookies.html')


def home_view(request):
    return _render(request, 'home.html')


def wip_view(request):
    return _render(request, 'wip.html')


def gaming_view(request):
    return _render(request, 'gaming.html')


def music_view(request):
    return _render(request, 'music.html')


def contact_view(request):
    return _render(request, 'contact.html')


def coding_view(request):
    return _render(request, 'coding.html')


def wd2_view(request):
    return _render(request, 'wd2.html')


def landing_view(request):
    if 'landed' in request.COOKIES or request.user_agent.is_touch_capable:
        response = home_view(request)
    elif not request.user_agent.is_touch_capable:
        response = wd2_view(request)
        response.set_cookie('landed', '1')
    return response


def submit_view(request):
    return _render(request, 'submit.html')


def _render(request, target, **kwargs):
    theme = 'hotline_miami'
    primary = 'aqua'
    secondary = 'purple'
    if 'theme' in request.COOKIES:
        theme = request.COOKIES['theme']

    try:
        theme_model = Theme.objects.get(key=theme)
    except:
        theme_model = None

    gp_color = request.GET.get('primary')
    gs_color = request.GET.get('secondary')
    if gp_color and gs_color:
        primary = gp_color
        secondary = gs_color
        theme = request.GET.get('theme_name')
    elif theme_model:
        primary = theme_model.primary
        secondary = theme_model.secondary
    elif 'primary' in request.COOKIES and 'secondary' in request.COOKIES:
        primary = request.COOKIES['primary']
        secondary = request.COOKIES['secondary']

    kwargs['gk_theme_primary'] = primary
    kwargs['gk_theme_secondary'] = secondary

    response = render(request, target, kwargs)
    response.set_cookie('theme', theme)
    response.set_cookie('primary', primary)
    response.set_cookie('secondary', secondary)
    return response


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
