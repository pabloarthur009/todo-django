# Requisitos do Sistema - ToDo List Django  

## **Requisitos Funcionais**  

### **1. Gerenciamento de Tarefas**  
- **RF01:** O sistema deve permitir a criação de novas tarefas (título, descrição, status).  
- **RF02:** O sistema deve listar todas as tarefas cadastradas.  
- **RF03:** O sistema deve exibir detalhes de uma tarefa específica.  
- **RF04:** O sistema deve permitir a edição de tarefas existentes.  
- **RF05:** O sistema deve permitir a exclusão de tarefas.  

### **2. Interface do Usuário**  
- **RF06:** O sistema deve ter uma página inicial listando todas as tarefas.  
- **RF07:** O sistema deve ter um formulário para adicionar/editar tarefas.  
- **RF08:** O sistema deve exibir mensagens de confirmação após ações (criar/editar/excluir).  

### **3. Funcionalidades Extras (Opcionais)**  
- **RF09:** O sistema pode permitir marcar tarefas como concluídas.  
- **RF10:** O sistema pode filtrar tarefas por status (concluídas/pendentes).  

---

## **Requisitos Não Funcionais**  

### **1. Desempenho**  
- **RNF01:** O sistema deve carregar a lista de tarefas em menos de 2 segundos.  

### **2. Segurança**  
- **RNF02:** O sistema não deve permitir injeção de SQL/XSS.  

### **3. Usabilidade**  
- **RNF03:** O sistema deve ser responsivo (funcionar em desktop e mobile).  

### **4. Tecnologias**  
- **RNF04:** O sistema deve ser desenvolvido em **Django (Python)**.  
- **RNF05:** O sistema deve usar **SQLite** (para desenvolvimento) e **PostgreSQL** (para produção opcional).  