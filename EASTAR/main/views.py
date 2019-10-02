from django.shortcuts import render

# Create your views here.


def Base(request):
    return render(request, 'main/index.html', {})


def About(request):
    return render(request, 'main/about.html', {})


def Contacts(request):
    return render(request, 'main/contacts.html', {})


def Values(request):
    return render(request, 'main/values.html', {})


def Technology(request):
    return render(request, 'main/technology.html', {})


def Technologies(request, pk):
    return render(request, f'main/technology {pk}.html', {})
