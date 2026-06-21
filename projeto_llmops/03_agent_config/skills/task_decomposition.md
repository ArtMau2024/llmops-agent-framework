# 🧩 SKILL — TASK DECOMPOSITION (Decomposição Estruturada de Tarefas)

---

## 🎯 1. OBJETIVO DA SKILL

A skill de task_decomposition é responsável por dividir problemas complexos em partes menores, claras e executáveis.

Seu objetivo é:

- reduzir complexidade
- permitir execução incremental
- evitar sobrecarga lógica
- garantir organização da solução
- viabilizar construção por MVPs

---

## 🧠 2. QUANDO UTILIZAR

Esta skill deve ser ativada quando houver:

- problemas complexos com múltiplas etapas
- necessidade de dividir tarefas
- construção de soluções grandes (pipelines, sistemas)
- dificuldade de execução direta
- necessidade de organização operacional

---

## 📊 3. PAPEL NO SISTEMA

A skill de task_decomposition pode atuar como:

---

### ✅ Skill principal

Quando o objetivo for:

- dividir problema em etapas
- estruturar execução detalhada
- organizar fluxo de trabalho

---

### ✅ Skill de suporte

Combinada com:

- planning → estruturar plano geral
- reasoning → validar lógica da divisão
- code_generation → implementar cada etapa

---

## ⚙️ 4. LÓGICA DE EXECUÇÃO

A execução deve seguir obrigatoriamente:

---

### 1. Identificação do problema

- compreender o problema completo
- identificar objetivo final
- entender escopo da tarefa

---

### 2. Segmentação do problema

- dividir em blocos principais
- identificar partes independentes
- separar responsabilidades

---

### 3. Estruturação das etapas

- organizar sequência lógica
- definir relação entre etapas
- mapear dependências

---

### 4. Refinamento das tarefas

- quebrar etapas grandes em subetapas
- garantir que cada parte seja executável
- eliminar ambiguidades

---

### 5. Preparação para execução

- definir ordem clara de execução
- indicar ponto de início
- preparar integração com outras skills

---

## 🧩 5. ESTRUTURA DE RESPOSTA

---

### 📘 Modo Mentor

1. Contexto do problema  
2. Divisão em blocos principais  
3. Explicação de cada etapa  
4. Relação entre etapas  
5. Ordem de execução  

---

### ⚙️ Modo Executor

1. Etapas definidas  
2. Sequência de execução  
3. Dependências críticas  
4. Próxima ação  

---

## 🔄 6. INTEGRAÇÃO COM OUTRAS SKILLS

A skill deve ser combinada conforme necessidade:

---

### 🔗 Combinações comuns

- task_decomposition + planning → estrutura completa do projeto
- task_decomposition + reasoning → divisão lógica consistente
- task_decomposition + code_generation → execução por etapas
- task_decomposition + validation → revisão da estrutura

---

## ✅ 7. VALIDAÇÃO INTERNA

A skill deve validar:

- o problema foi corretamente dividido?
- todas as etapas são executáveis?
- existem lacunas entre as etapas?
- a sequência faz sentido?

---

## ⚠️ 8. DETECÇÃO DE RISCO

A skill deve identificar:

- etapas mal definidas
- dependências não tratadas
- divisão superficial
- fragmentação excessiva

---

### Ação obrigatória:

- ajustar decomposição
- reorganizar etapas
- garantir clareza antes de execução

---

## 🧾 9. PADRÕES DE QUALIDADE

A decomposição deve:

- ser clara e objetiva
- evitar ambiguidade
- manter coerência com o objetivo final
- facilitar execução

---

### ✅ Boas práticas obrigatórias

- cada etapa deve ser executável isoladamente
- evitar etapas genéricas ("processar dados")
- manter granularidade adequada (nem muito grande nem muito pequena)
- garantir sequência lógica clara

---

## 🚫 10. PROIBIÇÕES

A skill não deve:

- dividir sem entender o problema
- criar etapas vagas
- ignorar dependências
- gerar estrutura difícil de executar
- fragmentar excessivamente sem necessidade

---

## 🎯 11. CRITÉRIO DE QUALIDADE

A execução é considerada correta quando:

- todas as etapas são claras
- cada etapa pode ser executada isoladamente
- não há lacunas na solução
- a sequência de execução é lógica

---

## 🔁 12. RELAÇÃO COM O SISTEMA (agent_rules)

Esta skill suporta diretamente:

- 5.3.1 → classificação (problemas complexos)
- 5.3.2 → combinação com planning
- 5.3.3 → execução estruturada
- 6.x → validação da estrutura

---

## 🚀 13. OBJETIVO FINAL

Garantir que o agente:

- consiga lidar com problemas complexos
- execute de forma organizada
- construa soluções escaláveis
- mantenha clareza durante todo o processo