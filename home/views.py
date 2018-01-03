from django.shortcuts import render

try:
    from charon import charon
    charon_avail = True
except:
    charon_avail = False

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


def wd2_page(request):
    return render(request, 'wd2.html')


def landing_page(request):
    if 'landed' in request.COOKIES:
        response = home_page(request)
    else:
        response = wd2_page(request)
        response.set_cookie('landed', '1')
    return response


def charon_page(request):
    preview = ''
    output = ''
    if(request.GET.get('upload_github_button')):
        username = request.GET.get('username_text')
        reponame = request.GET.get('reponame_text')
        cogname = request.GET.get('cogname_text')
        if charon_avail:
            try:
                preview = charon.get_info(username, reponame, cogname)
            except Exception as e:
                print(str(e))

    return render(
        request, 'charon.html', {'preview': preview, 'output': output})
