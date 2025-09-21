from django.shortcuts import render, redirect, get_object_or_404   
from .models import Receta
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def registrar_receta(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_receta']
        descripcion = request.POST['descripcion_receta']
        precio = request.POST['precio_receta']
        tipo = request.POST['tipo_receta']
        extras = request.POST['extra_receta']

        Receta.objects.create(
            nombre=nombre, 
            descripcion=descripcion, 
            precio=precio,
            tipo=tipo,
            extras=extras
        )
        return redirect("lista_recetas")
        
    return render(request, 'registrar_receta.html')

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'lista_recetas.html', {'recetas': recetas})

def eliminar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    return redirect("lista_recetas")