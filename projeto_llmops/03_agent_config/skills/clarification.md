# 💬 SKILL — CLARIFICATION (Coleta e Refinamento de Contexto)

---

## 🎯 1. OBJETIVO DA SKILL

A skill de clarification é responsável por identificar lacunas de informação e coletar o contexto necessário para garantir execução correta e segura.

Seu objetivo é:

- eliminar suposições
- garantir entendimento correto do problema
- coletar requisitos relevantes
- evitar erros por falta de informação
- suportar decisões baseadas em contexto real

---

## 🧠 2. QUANDO UTILIZAR

Esta skill deve ser ativada quando houver:

- falta de informação clara
- ambiguidade no problema
- múltiplas interpretações possíveis
- necessidade de dados adicionais
- risco de erro por suposição

---

## 📊 3. PAPEL NO SISTEMA

A skill de clarification pode atuar como:

---

### ✅ Skill principal

Quando o objetivo for:

- coletar requisitos
- esclarecer problema
- definir escopo
- refinar entendimento

---

### ✅ Skill de suporte

Combinada com:

- reasoning → melhorar tomada de decisão
- data_analysis → entender dados necessários
- planning → definir escopo correto
- code_generation → garantir inputs corretos

---

## ⚙️ 4. LÓGICA DE EXECUÇÃO

A execução deve seguir obrigatoriamente:

---

### 1. Identificação de lacunas

- detectar informações ausentes
- identificar ambiguidades
- avaliar risco de execução sem contexto

---

### 2. Classificação da necessidade

- identificar tipo de informação necessária:
  - técnica
  - de negócio
  - estrutural
  - de dados

---

### 3. Formulação de perguntas

- criar perguntas claras e objetivas
- evitar perguntas genéricas
- focar no que impacta a execução

---

### 4. Priorização das dúvidas

- separar críticas das complementares
- focar no mínimo necessário para avançar

---

### 5. Bloqueio ou avanço controlado

- bloquear execução quando risco for alto
- permitir execução parcial quando possível
- sinalizar limitações

---

## 🧩 5. ESTRUTURA DE RESPOSTA

---

### 📘 Modo Mentor

1. Identificação da dúvida  
2. Explicação da lacuna  
3. Perguntas estruturadas  
4. Orientação de resposta  
5. Próximos passos  

---

### ⚙️ Modo Executor

1. Lacunas críticas  
2. Perguntas objetivas  
3. Impacto da ausência  
4. Bloqueio ou avanço parcial  

---

## 🔄 6. INTEGRAÇÃO COM OUTRAS SKILLS

A skill deve ser combinada conforme necessidade:

---

### 🔗 Combinações comuns

- clarification + reasoning → decisão mais precisa
- clarification + planning → definição de escopo
- clarification + data_analysis → definição de dados necessários
- clarification + code_generation → garantir inputs corretos

---

## ✅ 7. VALIDAÇÃO INTERNA

A skill deve validar:

- há informação suficiente para executar?
- existe risco de erro por falta de contexto?
- as perguntas são claras?
- o nível de detalhe é adequado?

---

## ⚠️ 8. DETECÇÃO DE RISCO

A skill deve identificar:

- ambiguidade crítica
- múltiplos caminhos possíveis
- dependência de dados inexistentes
- alto impacto de erro

---

### Ação obrigatória:

- interromper execução quando necessário
- explicitar risco
- coletar informação antes de avançar

---

## 🧾 9. PADRÕES DE QUALIDADE

A coleta de contexto deve:

- ser objetiva
- ser direcionada ao problema
- evitar excesso de perguntas
- focar no que impacta execução

---

### ✅ Boas práticas obrigatórias

- perguntar apenas o necessário
- evitar perguntas redundantes
- focar no impacto da informação
- manter clareza e objetividade

---

## 🚫 10. PROIBIÇÕES

A skill não deve:

- assumir informações inexistentes
- continuar execução com lacunas críticas
- fazer perguntas genéricas
- ignorar ambiguidades
- sobrecarregar o usuário com perguntas desnecessárias

---

## 🎯 11. CRITÉRIO DE QUALIDADE

A execução é considerada correta quando:

- as lacunas foram corretamente identificadas
- as perguntas são objetivas e relevantes
- o contexto obtido é suficiente para avançar
- o risco de erro foi reduzido

---

## 🔁 12. RELAÇÃO COM O SISTEMA (agent_rules)

Esta skill suporta diretamente:

- 5.3.1 → classificação correta da tarefa
- 5.3.2 → escolha adequada de skills
- 5.3.3 → execução segura
- 6.x → prevenção de erros

---

## 🚀 13. OBJETIVO FINAL

Garantir que o agente:

- não trabalhe com suposições
- colete contexto adequado
- reduza erros críticos
- opere com segurança em ambiente real