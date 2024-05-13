from django.shortcuts import render
from mycv.models import GeneralSetting


def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    site_myname = GeneralSetting.objects.get(name='site_myname').parameter
    site_aboutme = GeneralSetting.objects.get(name='site_aboutme').parameter
    site_bronse = GeneralSetting.objects.get(name='site_bronse').parameter
    site_gold = GeneralSetting.objects.get(name='site_gold').parameter
    site_diamond = GeneralSetting.objects.get(name='site_diamond').parameter

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'site_myname': site_myname,
        'site_aboutme': site_aboutme,
        'site_bronse': site_bronse,
        'site_gold': site_gold,
        'site_diamond': site_diamond,
    }
    return render(request, 'index.html', context=context)

def contact(request):
    return render(request, 'contact.html')
