# 💻 SKILL — CODE GENERATION (Geração Estruturada de Código)

---

## 🎯 1. OBJETIVO DA SKILL

A skill de code_generation é responsável por gerar código funcional, estruturado, validável e alinhado com o projeto.

Seu objetivo é:

- transformar lógica em código executável
- garantir qualidade e clareza da implementação
- substituir soluções manuais (ex: Excel)
- viabilizar automação e escalabilidade

---

## 🧠 2. QUANDO UTILIZAR

Esta skill deve ser ativada quando houver:

- necessidade de implementação técnica
- geração de scripts Python (pandas, automação, ETL)
- criação de análises programáticas
- construção de relatórios automatizados
- substituição de processos manuais

---

## 📊 3. PAPEL NO SISTEMA

A skill de code_generation pode atuar como:

---

### ✅ Skill principal

Quando o objetivo principal for:

- gerar código
- implementar solução técnica
- automatizar processo

---

### ✅ Skill de suporte

Combinada com:

- reasoning → definir lógica antes do código
- data_analysis → estruturar manipulação de dados
- validation → garantir qualidade e funcionamento

---

## ⚙️ 4. LÓGICA DE EXECUÇÃO

A execução deve seguir obrigatoriamente:

---

### 1. Entendimento da necessidade

- identificar o objetivo do código
- mapear entrada e saída esperada
- identificar restrições técnicas

---

### 2. Definição da lógica

- estruturar a solução antes de codar
- definir etapas do processamento
- validar coerência lógica

---

### 3. Estruturação do código

- organizar em etapas claras
- separar responsabilidades (funções, blocos)
- garantir legibilidade

---

### 4. Implementação

- gerar código funcional
- utilizar boas práticas (nomes claros, comentários)
- evitar redundâncias

---

### 5. Preparação para validação

- incluir formas de testar
- prever outputs esperados
- indicar pontos críticos

---

## 🧩 5. ESTRUTURA DE RESPOSTA

---

### 📘 Modo Mentor

1. Objetivo do código  
2. Explicação da lógica aplicada  
3. Código com comentários  
4. Como executar  
5. Como validar  

---

### ⚙️ Modo Executor

1. Código direto  
2. Requisitos de execução  
3. Pontos críticos  
4. Validação rápida  

---

## 🔄 6. INTEGRAÇÃO COM OUTRAS SKILLS

A skill deve ser combinada conforme necessidade:

---

### 🔗 Combinações comuns

- code_generation + reasoning → lógica antes do código
- code_generation + data_analysis → manipulação de dados
- code_generation + validation → verificação de resultado
- code_generation + planning → organização de pipeline

---

## ✅ 7. VALIDAÇÃO INTERNA

A skill deve validar:

- o código resolve o problema proposto?
- a lógica está correta?
- o código é executável?
- há dependências faltando?

---

## ⚠️ 8. DETECÇÃO DE RISCO

A skill deve identificar:

- dependências não definidas
- dados não especificados
- ambiguidade no input
- complexidade não tratada

---

### Ação obrigatória:

- sinalizar o risco
- solicitar clarificação
- evitar gerar código inválido

---

## 🧾 9. PADRÕES DE QUALIDADE

O código gerado deve:

- ser legível
- ter nomes claros de variáveis
- evitar duplicação de lógica
- seguir boas práticas básicas de engenharia

---

### ✅ Boas práticas obrigatórias

- uso de funções quando necessário
- organização em blocos lógicos
- comentários quando necessário
- evitar hardcode sempre que possível

---

## 🚫 10. PROIBIÇÕES

A skill não deve:

- gerar código sem entender o problema
- gerar código não executável
- assumir estrutura de dados inexistente
- ignorar validação
- entregar código sem contexto

---

## 🎯 11. CRITÉRIO DE QUALIDADE

A execução é considerada correta quando:

- o código funciona corretamente
- a lógica está consistente
- a solução é reproduzível
- o código pode ser mantido e entendido

---

## 🔁 12. RELAÇÃO COM O SISTEMA (agent_rules)

Esta skill suporta diretamente:

- 5.3.1 → classificação (quando envolve implementação)
- 5.3.2 → ativação principal em tasks técnicas
- 5.3.3 → execução estruturada
- 6.x → validação e qualidade

---

## 🚀 13. OBJETIVO FINAL

Garantir que o agente:

- transforme problemas em soluções executáveis
- produza código confiável
- reduza dependência de Excel/manual
- construa base para automação e escala