from django.shortcuts import render
from datetime import datetime


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


def inicio(request):

    contexto = {
        'first_name': 'John',
        'last_name': 'Doe',

        'my_dict': {
            'key': 'Valor del diccionario'
        },

        'my_object': Persona('Oscar'),

        'my_list': [10, 20, 30],

        'usuario_autenticado': True,

        'numeros': [10, 20, 30, 40],

        'django': 'the web framework for perfectionists with deadlines',

        'my_date': datetime.now(),
    }

    return render(request, 'inicio.html', contexto)