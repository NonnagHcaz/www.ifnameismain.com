from django.shortcuts import render

import json

try:
    from kharon import kharon
    kharon_avail = True
except Exception:
    kharon_avail = False

# from django.http import HttpResponse


def themes_view(request):
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
