from django.shortcuts import render
from .models import Cliente, Asesoramiento, Cita


def index(request):
    return render(request, "estudiojuridico/index.html")


def cliente_list(request):
    query = Cliente.objects.all()
    context = {"object_list": query}
    return render(request, "estudiojuridico/cliente_list.html", context)


def asesoramiento_list(request):
    query = Asesoramiento.objects.all()
    context = {"object_list": query}
    return render(request, "estudiojuridico/asesoramiento_list.html", context)


def cita_list(request):
    query = Cita.objects.all()
    context = {"object_list": query}
    return render(request, "estudiojuridico/cita_list.html", context)


# def cliente_create(request):
#     pass

# def asesoramiento_create(request):
#     pass

# def cita_create(request):
#     pass
