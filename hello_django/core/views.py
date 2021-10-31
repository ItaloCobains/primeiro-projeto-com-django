from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome}, de {idade} anos</h1>')

def soma(request, n1, n2):
    r = n1 + n2
    return HttpResponse(f'<h1>A soma entre {n1} e {n2} é = {r}</h1>')

def sub(request, n1, n2):
    r = n1 - n2
    return HttpResponse(f'<h1>A subtração entre {n1} e {n2} é = {r}</h1>')

def multi(request, n1, n2):
    r = n1 * n2
    return HttpResponse(f'<h1>A multiplicação entre {n1} e {n2} é = {r}</h1>')

def div(request, n1, n2):
    r = n1 / n2
    return HttpResponse(f'<h1>A divisao entre {n1} e {n2} é = {r}</h1>')
