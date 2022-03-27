from django.shortcuts import render
from django.http import HttpResponse


def index(request, exception=None):
    ''' Entry for welcome and 404s '''
    return render(request, "index.html")


def error(request, exception=None):
    '''
        handler for 500 respsonses
    '''
    return HttpResponse(
        f'''<p>Error: {exception}</p>
        To learn about how to use this API,
        head to <a href='https://apis.nehemie.dev/bkg-emailer/welcome'>
        https://apis.nehemie.dev/bkg-emailer/welcome</a>
        '''
    )
