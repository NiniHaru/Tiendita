from django.shortcuts import render
from django.http import HttpResponse
from tiendita.models import Cliente, Producto
from django.contrib import messages


def index(request):
    productos = Producto.objects.all()
    c = 0
    for producto in productos:
        c = c + 1
    l = c - 4
    productos = Producto.objects.all()[l:]
    return render(request, 'index.html', {"productos":productos})
    

def F(request):
    return render(request, 'F.html', )


def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {"productos":productos})


def carrito(request):    
    return render(request, 'carrito.html', )
    

def registro(request):
    if request.method=='POST':   
        rut=request.POST['rut']
        nombre=request.POST['nombre']
        apellido=request.POST['apellido']
        fono=request.POST['fono']
        correo=request.POST['correo']
        contra=request.POST['contra']
        c=Cliente(per_rut=rut, per_nombre=nombre, per_apellido=apellido, cli_fono=fono, per_correo=correo, per_contra=contra)
        c.save()
        messages.success(request, 'Registro exitoso de '+request.POST['nombre']+', ya puede iniciar sesión')
        return render(request, 'registro.html', )
    else:
        return render(request, 'registro.html', )


def login(request):
    if request.method=='POST':
        try:
            clientee=Cliente.objects.get(per_correo=request.POST['correo'], per_contra=request.POST['contra'])
            request.session['per_correo']=clientee.per_correo
            return render(request, 'index.html', )
        except Cliente.DoesNotExist as e:
            messages.success(request, 'Correo o contraseña incorrecta ')
    return render(request, 'login.html', )


def cerrarSesion(request):
    try:
        del request.session['per_correo']
    except:
        return render(request, 'index.html', )
    return render(request, 'index.html', )

