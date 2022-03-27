from django.shortcuts import render


def index(request, exception=None):
    ''' Entry for welcome and 404s '''
    return render(request, "index.html")
