from django.shortcuts import render, get_object_or_404
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tasks/lista.html', {'tarefas': tarefas})

def detalhe_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, 'tasks/detalhe.html', {'tarefa': tarefa})