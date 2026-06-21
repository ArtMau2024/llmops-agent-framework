# 🧠 SKILL — REASONING (Raciocínio Estruturado)

---

## 🎯 1. OBJETIVO DA SKILL

A skill de reasoning é responsável por estruturar o pensamento lógico do agente antes de qualquer execução.

Seu objetivo é:

- evitar decisões impulsivas
- garantir coerência da solução
- estruturar problemas complexos
- suportar a escolha de abordagem

---

## 🧠 2. QUANDO UTILIZAR

Esta skill deve ser ativada quando houver:

- necessidade de tomada de decisão
- resolução de problemas complexos
- múltiplas abordagens possíveis
- dúvidas sobre a melhor estratégia
- análise antes da execução

---

## 📊 3. PAPEL NO SISTEMA

A skill de reasoning pode atuar como:

---

### ✅ Skill principal

Quando o problema exigir:

- definição de estratégia
- decisão técnica
- estruturação de solução

---

### ✅ Skill de suporte

Combinada com:

- data_analysis → interpretar resultados
- code_generation → definir lógica antes do código
- planning → estruturar estratégia

---

## ⚙️ 4. LÓGICA DE EXECUÇÃO

A execução deve seguir obrigatoriamente:

---

### 1. Compreensão do problema

- identificar o objetivo real
- mapear restrições
- validar entendimento

---

### 2. Decomposição lógica

- quebrar o problema em partes
- identificar dependências
- priorizar etapas

---

### 3. Exploração de soluções

- listar possíveis abordagens
- avaliar vantagens e desvantagens
- considerar riscos

---

### 4. Tomada de decisão

- escolher a melhor abordagem
- justificar tecnicamente
- explicar impacto

---

### 5. Preparação para execução

- estruturar próximos passos
- alinhar com o sistema (skills + modos)

---

## 🧩 5. ESTRUTURA DE RESPOSTA

---

### 📘 Modo Mentor

1. Entendimento do problema  
2. Estrutura lógica da solução  
3. Explicação das opções  
4. Decisão e justificativa  
5. Próximos passos  

---

### ⚙️ Modo Executor

1. Premissas adotadas  
2. Decisão tomada  
3. Justificativa resumida  
4. Próxima ação  

---

## 🔄 6. INTEGRAÇÃO COM OUTRAS SKILLS

A skill deve ser combinada conforme necessidade:

---

### 🔗 Combinações comuns

- reasoning + data_analysis → interpretação estruturada
- reasoning + code_generation → definição antes do código
- reasoning + planning → estratégia completa
- reasoning + validation → revisão lógica

---

## ✅ 7. VALIDAÇÃO INTERNA

A skill deve validar:

- o problema foi corretamente entendido?
- a solução é coerente?
- há lacunas não tratadas?
- existe risco de erro lógico?

---

## ⚠️ 8. DETECÇÃO DE RISCO

A skill deve identificar:

- ambiguidade no problema
- múltiplas interpretações possíveis
- falta de dados
- complexidade não tratada

---

### Ação obrigatória:

- sinalizar o risco
- solicitar clarificação
- evitar decisão precipitada

---

## 🚫 9. PROIBIÇÕES

A skill não deve:

- assumir entendimento sem validar
- pular etapas de análise
- tomar decisões sem justificativa
- ignorar alternativas relevantes
- gerar soluções baseadas em suposição

---

## 🎯 10. CRITÉRIO DE QUALIDADE

A execução da skill é considerada correta quando:

- o raciocínio é claro e estruturado
- a decisão é justificável
- o problema é completamente abordado
- não há inconsistências lógicas

---

## 🔁 11. RELAÇÃO COM O SISTEMA (agent_rules)

Esta skill dá suporte direto a:

- 5.3.1 → classificação da tarefa
- 5.3.2 → escolha de skills
- 5.3.3 → execução estruturada
- 6.x → validação e qualidade

---

## 🚀 12. OBJETIVO FINAL

Garantir que o agente:

- pense antes de agir
- tome decisões consistentes
- evite erros estruturais
- construa soluções sustentáveis