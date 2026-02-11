from django.shortcuts import render

def index(request):
    context= {'curso': 'desenvolvimento de sistemas'}
    return render(request, 'index.html', context)

def contato(request):
    context= {'nome': 'Instituto Federal de Santa Catarina',
              'telefone': 'Telefone: (47) 3363-5251', 
              'email': 'E-mail: contato@ifsc.edu.br'}
    return render(request, 'contato.html', context)
