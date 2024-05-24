from django.shortcuts import render, redirect, get_object_or_404
from mycv.models import GeneralSetting, ImageSetting, SocialMedia, Document


def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    site_myname = GeneralSetting.objects.get(name='site_myname').parameter
    site_aboutme = GeneralSetting.objects.get(name='site_aboutme').parameter
    site_bronse = GeneralSetting.objects.get(name='site_bronse').parameter
    site_gold = GeneralSetting.objects.get(name='site_gold').parameter
    site_diamond = GeneralSetting.objects.get(name='site_diamond').parameter
    social_medias = SocialMedia.objects.all()
    documents = Document.objects.all()

    # Resimler

    site_favicon = ImageSetting.objects.get(name='site_favicon').file
    about_me_img = ImageSetting.objects.get(name='about_me_img').file

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'site_myname': site_myname,
        'site_aboutme': site_aboutme,
        'site_bronse': site_bronse,
        'site_gold': site_gold,
        'site_diamond': site_diamond,
        'site_favicon': site_favicon,
        'about_me_img': about_me_img,
        'social_medias': social_medias,
        'documents': documents,
    }
    return render(request, 'index.html', context=context)

def contact(request):
    return render(request, 'contact.html')

def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)


