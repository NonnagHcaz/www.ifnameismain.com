from django.shortcuts import render

try:
    from kharon import kharon
    kharon_avail = True
except:
    kharon_avail = False

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


def kharon_page(request):
    preview = ''
    output = ''
    if request.GET.get('upload_github_button'):
        username = request.GET.get('username_text')
        reponame = request.GET.get('reponame_text')
        cogname = request.GET.get('cogname_text')
        if kharon_avail:
            try:
                preview = kharon.get_info(username, reponame, cogname)
            except Exception as e:
                print(str(e))
        else:
            print('ERROR: kharon not found.')
    elif request.GET.get('convert_button'):
        contents = request.GET.get('upload_preview_textarea')
        print(contents)
        # formatted = kharon.format_info
    elif request.GET.get('export_button'):
        contents = request.GET.get('export_output_textarea')
        print(contents)
    return render(
        request, 'kharon.html', {'preview': preview, 'output': output})
