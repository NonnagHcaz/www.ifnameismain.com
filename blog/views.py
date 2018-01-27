from django.forms.models import model_to_dict
from django.shortcuts import render
from .models import Theme

# Create your views here.


def landing_view(request, **kwargs):
    if 'landed' in request.COOKIES or request.user_agent.is_touch_capable:
        response = home_view(request)
    else:
        response = home_view(request)
        response.set_cookie('landed', '1')
    return response


def home_view(request, **kwargs):
    return _render(request, 'home.html', **kwargs)


def _render(request, target, **kwargs):

    age = 60 * 60 * 24 * 7

    primary = request.GET.get('primary')
    secondary = request.GET.get('secondary')
    theme = request.GET.get('theme_name')

    try:
        theme_model = Theme.objects.get(key=theme)
    except Exception:
        theme_model = None

    if not (primary and secondary):
        if theme_model:
            primary = theme_model.primary
            secondary = theme_model.secondary
        elif 'primary' in request.COOKIES and 'secondary' in request.COOKIES:
            primary = request.COOKIES['primary']
            secondary = request.COOKIES['secondary']
        else:
            primary = 'aqua'
            secondary = 'purple'

    kwargs['gk_theme_primary'] = primary
    kwargs['gk_theme_secondary'] = secondary
    kwargs['gk_theme_data'] = [
        model_to_dict(model) for model in Theme.objects.all()]

    response = render(request, target, kwargs)
    response.set_cookie('primary', primary, max_age=age)
    response.set_cookie('secondary', secondary, max_age=age)
    return response
