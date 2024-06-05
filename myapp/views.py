from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User  # Asegúrate de agregar esta línea
from .forms import UserLoginForm, UserRegistrationForm, RegistroForm
from .models import Registro

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'myapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'myapp/signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'myapp/home.html')

@login_required
def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.creado_por = request.user
            registro.save()
            return redirect('listar')
    else:
        form = RegistroForm()
    return render(request, 'myapp/registrar.html', {'form': form})

@login_required
def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Registro.objects.filter(nombre__icontains=query)
    return render(request, 'myapp/search.html', {'results': results, 'query': query})

@login_required
def listar_view(request):
    registros = Registro.objects.all()
    return render(request, 'myapp/listar.html', {'registros': registros})

@login_required
def detalle_view(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    return render(request, 'myapp/detalle.html', {'registro': registro})

@login_required
def editar_view(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES, instance=registro)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.editado_por = request.user
            registro.save()
            return redirect('detalle', pk=registro.pk)
    else:
        form = RegistroForm(instance=registro)
    return render(request, 'myapp/editar.html', {'form': form, 'registro': registro})

@login_required
def eliminar_view(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    if request.method == 'POST':
        registro.delete()
        return redirect('listar')
    return render(request, 'myapp/eliminar.html', {'registro': registro})

@login_required
def listar_usuarios_view(request):
    usuarios = User.objects.all()
    return render(request, 'myapp/listar_usuarios.html', {'usuarios': usuarios})

@login_required
def registrar_usuario_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UserRegistrationForm()
    return render(request, 'myapp/registrar_usuario.html', {'form': form})

@login_required
def editar_usuario_view(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UserRegistrationForm(instance=usuario)
    return render(request, 'myapp/editar_usuario.html', {'form': form})

@login_required
def eliminar_usuario_view(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'myapp/eliminar_usuario.html', {'usuario': usuario})







