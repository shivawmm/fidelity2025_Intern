from django.shortcuts import render, HttpResponse

def setsession(request):
    request.session['sname'] = 'Steve'
    return HttpResponse('Session is set')

def getsession(request):
    name = request.session.get('sname')
    return HttpResponse(f'The name is {name}')