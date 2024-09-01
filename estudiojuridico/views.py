from django.shortcuts import redirect, render
from .forms import ClienteForm, AsesoramientoForm, CitaForm
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


def cliente_create(request):
    if request.method == "GET":
        form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    return render(request, "estudiojuridico/cliente_create.html", {"form": form})

def asesoramiento_create(request):
    if request.method == "GET":
        form = AsesoramientoForm()
    if request.method == "POST":
        form = AsesoramientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("asesoramiento_list")
    return render(request,"estudiojuridico/asesoramiento_create.html", {"form": form})

def cita_create(request):
    if request.method == "GET":
        form = CitaForm()
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cita_list")
    return render(request,"estudiojuridico/cita_create.html", {"form": form})
