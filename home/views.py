from django.shortcuts import render

import json

try:
    from kharon import kharon
    kharon_avail = True
except Exception:
    kharon_avail = False

# from django.http import HttpResponse


def about_page(request):
    return render(request, 'about.html')


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


def wd2_page(request):
    return render(request, 'wd2.html')


def landing_page(request):
    if 'landed' in request.COOKIES:
        response = home_page(request)
    else:
        response = wd2_page(request)
        response.set_cookie('landed', '1')
    return response


def kharon_page(request):
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
