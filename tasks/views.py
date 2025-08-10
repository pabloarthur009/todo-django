from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefa
from .forms import TarefaForm

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tasks/lista.html', {'tarefas': tarefas})

def detalhe_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, 'tasks/detalhe.html', {'tarefa': tarefa})

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tasks/form.html', {'form': form})

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('detalhe_tarefa', pk=pk)
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tasks/form.html', {'form': form})

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return redirect('lista_tarefas')