from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Usuario
from backend.models import Usuario
from .forms import UploadExcelForm
import pandas as pd


# Create your views here.


def mantenimiento(request):
    return render(request, 'mantenimiento_usuario.html')

def bienvenida(request):
    return render(request, 'bienvenida.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'inicio.html')

def usuarios(request):
    return render(request, 'usuarios.html')

def lista_usuarios(request):
    usuarios = Usuario.objects.all()  # Obtener todos los usuarios de la base de datos
    return render(request, 'usuarios.html', {'usuarios': usuarios})  # Corrige 'usuarios.html' con la extensión del archivo


    
def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home.html')
        else:
            messages.error(request, 'Correo electrónico o contraseña incorrectos.')
    return render(request, 'login.html')


def upload_excel(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            if excel_file.name.endswith('.xlsx'):
                df = pd.read_excel(excel_file)
                for index, row in df.iterrows():
                    usuario = Usuario(
                        id_usuario=row['id_usuario'],
                        user_name=row['user_name'],
                        password=row['password'],
                        email=row['email'],
                        sesion_activa=row['sesion_activa']
                    )
                    # Guarda la instancia en la base de datos
                    usuario.save()
                return HttpResponse('Carga masiva exitosa')
            else:
                return HttpResponse('El archivo no es un archivo Excel válido')
    else:
        form = UploadExcelForm()
    return render(request, 'upload_excel.html', {'form': form})