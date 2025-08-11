from django.urls import path
from . import views

app_name = 'tasks' 

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    
    path('nova/', views.criar_tarefa, name='criar_tarefa'),
    path('<int:pk>/', views.detalhe_tarefa, name='detalhe_tarefa'),
    path('<int:pk>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('<int:pk>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
]
