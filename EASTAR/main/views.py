from django.shortcuts import render
from .models import ContentText, PagePhoto, MainPagePhoto, TechnologiesText, TechnologiesMoreText

# Create your views here.


def Base(request):
    text = ContentText.objects.get(pk=1).text.replace("\r", "").split("\n")
    return render(request, 'main/index.html', {
        "text": text,
        "technologies": TechnologiesText.objects.all()
        })


def About(request):
    return render(request, 'main/about.html', {})


def Contacts(request):
    return render(request, 'main/contacts.html', {})


def Values(request):
    return render(request, 'main/values.html', {})


def Technology(request):
    return render(request, 'main/technology.html', {
        "technologies": TechnologiesText.objects.all()
    })


def Technologies(request, pk):
    text = TechnologiesText.objects.get(pk=pk).text.replace("\r", "").split("\n")
    moreText = TechnologiesMoreText.objects.get(pk=pk).text.replace("\r", "").split("\n")
    return render(request, f'main/technology.html', {
        "text": text,
        "moreText": moreText,
        "technologies": TechnologiesText.objects.all()
        
        })
