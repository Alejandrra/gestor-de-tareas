from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import RegistroUsuarioForm
from .models import Tarea

def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.estado = True
    tarea.save()
    return redirect('lista_tareas')

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    return redirect('lista_tareas')

def lista_tareas(request):
    if request.method == 'POST':
        # Manejar la adición de una nueva tarea
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')

        if titulo:  # Solo agregar si el título no está vacío
            nueva_tarea = Tarea(
                titulo=titulo,
                descripcion=descripcion,
                fecha_vencimiento=fecha_vencimiento,
                estado=False
            )
            nueva_tarea.save()
            return redirect('lista_tareas')

    # Manejo de los filtros de tareas
    filtro = request.GET.get('filtro', 'todas')
    if filtro == 'pendientes':
        tareas = Tarea.objects.filter(estado=False)
    elif filtro == 'completadas':
        tareas = Tarea.objects.filter(estado=True)
    else:
        tareas = Tarea.objects.all()
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Iniciar sesión automáticamente después del registro
            return redirect('lista_tareas')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/registro.html', {'form': form})
