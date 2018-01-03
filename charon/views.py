from django.shortcuts import render
import charon
# from django.http import HttpResponse


def charon_page(request):
    if(request.GET.get('upload_github_button')):
        username = request.GET.get('username_text')
        reponame = request.GET.get('reponame_text')
        cogname = request.GET.get('cogname_text')
        convert_to = request.GET.get('red_version')
        out = charon.get_info(username, reponame, cogname)
    else:
        out = 'test'
    return render(request, 'charon.html', {'preview': out})
