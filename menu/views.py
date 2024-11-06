from django.shortcuts import redirect, render
from django.utils import translation
from django.conf import settings  
from django.urls import reverse
from django.contrib import messages
from .models import Menu

def menu_view(request):
    menu_items = Menu.objects.filter(parent__isnull=True).prefetch_related('children')
    languages = settings.LANGUAGES

    context = {
       'menu_items': menu_items,
       'languages': languages,
    }
    
    return render(request, 'menu/index.html',context=context)

def switch_language(request, language):
    response = redirect(reverse('menu:menu_view')) 
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    translation.activate(language)
    messages.success(request, f'Ви перемкнулися на мову: {language}')
    return response


