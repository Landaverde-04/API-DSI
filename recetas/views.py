from django.shortcuts import render, redirect   
from .models import Receta
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def registrar_receta(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_receta']
        descripcion = request.POST['descripcion_receta']
        precio = request.POST['precio_receta']

        Receta.objects.create(
            nombre=nombre, 
            descripcion=descripcion, 
            precio=precio
        )
        return redirect("lista_recetas")
        
    return render(request, 'registrar_receta.html')