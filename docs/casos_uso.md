# Diagrama de Casos de Uso - ToDo List  

## **Atores**  
- **Usuário:** Responsável por interagir com as tarefas.  

## **Casos de Uso**  

### **1. Listar Tarefas**  
- **Descrição:** O usuário visualiza todas as tarefas cadastradas.  
- **Fluxo Principal:**  
  1. O usuário acessa a página inicial.  
  2. O sistema exibe a lista de tarefas.  

### **2. Criar Tarefa**  
- **Descrição:** O usuário adiciona uma nova tarefa.  
- **Fluxo Principal:**  
  1. O usuário clica em "Nova Tarefa".  
  2. O sistema exibe um formulário.  
  3. O usuário preenche os dados e clica em "Salvar".  
  4. O sistema redireciona para a lista de tarefas.  

### **3. Editar Tarefa**  
- **Descrição:** O usuário modifica uma tarefa existente.  
- **Fluxo Principal:**  
  1. O usuário clica em "Editar" em uma tarefa.  
  2. O sistema exibe o formulário preenchido.  
  3. O usuário altera os dados e clica em "Salvar".  
  4. O sistema redireciona para a lista de tarefas.  

### **4. Excluir Tarefa**  
- **Descrição:** O usuário remove uma tarefa.  
- **Fluxo Principal:**  
  1. O usuário clica em "Excluir" em uma tarefa.  
  2. O sistema solicita confirmação.  
  3. O usuário confirma.  
  4. O sistema remove a tarefa e atualiza a lista.  

---

## **Diagrama de Casos de Uso (Texto)**  
```plaintext
+-------------------+     +---------------------+  
|     USUÁRIO       |     |    SISTEMA TODO     |  
+-------------------+     +---------------------+  
|                   |     |                     |  
| 1. Listar Tarefas |<--->| - Exibe lista       |  
| 2. Criar Tarefa   |<--->| - Valida dados      |  
| 3. Editar Tarefa  |<--->| - Atualiza tarefa   |  
| 4. Excluir Tarefa |<--->| - Remove tarefa     |  
|                   |     |                     |  
+-------------------+     +---------------------+  
