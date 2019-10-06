from django.shortcuts import render
from .models import ContentText, PagePhoto, MainPagePhoto, Technologies

# Create your views here.


def Base(request):
    return render(request, 'main/index.html', {
        "text": ContentText.objects.get(pk=1).textRU.replace("\r", "").split("\n"),
        "header": ContentText.objects.get(pk=1).titleRU,
        "technologies": Technologies.objects.all()
        })


def About(request):
    return render(request, 'main/about.html', {})


def Contacts(request):
    return render(request, 'main/contacts.html', {})


def Values(request):
    return render(request, 'main/values.html', {})


def Technology(request):
    return render(request, 'main/technology.html', {
        "technologies": Technologies.objects.all(),
    })


def TechnologiesView(request, pk):
    text = Technologies.objects.get(pk=pk).textRU.replace("\r", "").split("\n")
    return render(request, f'main/technology.html', {
        "text": text,
        "technologies": Technologies.objects.all(),
        "moreText": Technologies.objects.get(pk=pk).textAddRU.replace("\r", "").split("\n"),
        })
