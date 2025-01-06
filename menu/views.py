from django.shortcuts import render, get_object_or_404, redirect
from .models import Platillo, Comentario
from .forms import PlatilloForm
from django.utils.timezone import now

# Pantalla principal: Mostrar menú del día
def menu_principal(request):
    platillos = Platillo.objects.filter(fecha='2025-01-01')  # Cambia a la fecha actual dinámicamente
    return render(request, 'menu/menu_principal.html', {'platillos': platillos})

# Pantalla de detalles de un platillo
def detalle_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    return render(request, 'menu/detalle_platillo.html', {'platillo': platillo})

# Agregar platillo
def agregar_platillo(request):
    if request.method == 'POST':
        form = PlatilloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_principal')
    else:
        form = PlatilloForm()
    # Obtener todos los platillos para mostrar en la tabla
    platillos = Platillo.objects.all()
    return render(request, 'menu/agregar_platillo.html', {'form': form, 'platillos': platillos})

# Editar platillo
def editar_platillo(request, platillo_id):
    # Obtener el platillo correspondiente por id
    platillo = get_object_or_404(Platillo, id=platillo_id)
    
    # Si el método de la solicitud es POST, procesamos el formulario
    if request.method == 'POST':
        form = PlatilloForm(request.POST, instance=platillo)
        
        # Si el formulario es válido, guardamos el platillo y redirigimos al detalle
        if form.is_valid():
            form.save()
            return redirect('detalle_platillo', platillo_id=platillo.id)
    else:
        form = PlatilloForm(instance=platillo)  # Si no es POST, cargamos el formulario con los datos actuales del platillo
    
    # Renderizar la plantilla de edición de platillo
    return render(request, 'menu/editar_platillo.html', {'form': form, 'platillo': platillo})
# Eliminar platillo
def eliminar_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    if request.method == 'POST':
        platillo.delete()
        return redirect('menu_principal')
    return render(request, 'menu/eliminar_platillo.html', {'platillo': platillo})

def agregar_comentario(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    
    # Obtener los comentarios existentes
    comentarios = platillo.comentarios.all()
    
    if request.method == 'POST':
        usuario = request.POST['usuario']
        comentario = request.POST['comentario']
        calificacion = int(request.POST['calificacion'])
        
        Comentario.objects.create(platillo=platillo, usuario=usuario, comentario=comentario, calificacion=calificacion)
        
        # Actualiza calificación promedio
        comentarios = platillo.comentarios.all()  # Volver a obtener comentarios actualizados
        promedio = sum(c.calificacion for c in comentarios) / comentarios.count()
        platillo.calificacion_promedio = promedio
        platillo.save()

        return redirect('detalle_platillo', platillo_id=platillo.id)

    return render(request, 'menu/agregar_comentario.html', {'platillo': platillo, 'comentarios': comentarios})
def editar_comentario(request, platillo_id, comentario_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    comentario = get_object_or_404(Comentario, id=comentario_id, platillo=platillo)
    
    if request.method == 'POST':
        comentario.usuario = request.POST['usuario']
        comentario.comentario = request.POST['comentario']
        comentario.calificacion = int(request.POST['calificacion'])
        comentario.save()

        # Actualizar calificación promedio
        comentarios = platillo.comentarios.all()
        promedio = sum(c.calificacion for c in comentarios) / comentarios.count()
        platillo.calificacion_promedio = promedio
        platillo.save()

        return redirect('detalle_platillo', platillo_id=platillo.id)

    return render(request, 'menu/editar_comentario.html', {'platillo': platillo, 'comentario': comentario})
def eliminar_comentario(request, platillo_id, comentario_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    comentario = get_object_or_404(Comentario, id=comentario_id, platillo=platillo)
    
    if request.method == 'POST':
        comentario.delete()

        # Actualizar calificación promedio
        comentarios = platillo.comentarios.all()
        promedio = sum(c.calificacion for c in comentarios) / comentarios.count() if comentarios.count() > 0 else 0
        platillo.calificacion_promedio = promedio
        platillo.save()

        return redirect('detalle_platillo', platillo_id=platillo.id)

    return render(request, 'menu/eliminar_comentario.html', {'platillo': platillo, 'comentario': comentario})
