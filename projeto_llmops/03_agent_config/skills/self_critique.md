# 🔍 SKILL — SELF CRITIQUE (Autocrítica e Revisão de Qualidade)

---

## 🎯 1. OBJETIVO DA SKILL

A skill de self_critique é responsável por revisar criticamente as soluções geradas pelo agente, com foco em melhoria contínua, qualidade e prevenção de erros.

Seu objetivo é:

- identificar falhas e inconsistências
- melhorar respostas antes da entrega final
- evitar regressões no sistema
- elevar o padrão de qualidade das soluções
- complementar o processo de validation

---

## 🧠 2. QUANDO UTILIZAR

Esta skill deve ser ativada quando houver:

- soluções complexas ou críticas
- outputs antes da entrega final
- múltiplas decisões envolvidas
- necessidade de revisão de qualidade
- dúvida sobre robustez da solução

---

## 📊 3. PAPEL NO SISTEMA

A skill de self_critique pode atuar como:

---

### ✅ Skill principal

Quando o objetivo for:

- revisar solução completa
- melhorar qualidade da resposta
- realizar análise crítica detalhada

---

### ✅ Skill de suporte

Combinada com:

- validation → garantir correção técnica
- reasoning → revisar lógica
- code_generation → revisar código
- data_analysis → revisar interpretação

---

## ⚙️ 4. LÓGICA DE EXECUÇÃO

A execução deve seguir obrigatoriamente:

---

### 1. Revisão do objetivo

- confirmar qual era o objetivo da solução
- validar se o resultado atende ao propósito

---

### 2. Revisão da lógica

- verificar coerência da solução
- identificar falhas ou lacunas
- revisar decisões tomadas

---

### 3. Revisão da execução

- avaliar qualidade do código ou análise
- verificar clareza e organização
- identificar pontos frágeis

---

### 4. Identificação de melhorias

- sugerir otimizações
- apontar simplificações possíveis
- propor ajustes estruturais

---

### 5. Consolidação

- classificar qualidade da solução
- indicar se está pronta para entrega ou não

---

## 🧩 5. ESTRUTURA DE RESPOSTA

---

### 📘 Modo Mentor

1. Objetivo da revisão  
2. Análise crítica da solução  
3. Problemas encontrados  
4. Sugestões de melhoria  
5. Versão aprimorada (se aplicável)  

---

### ⚙️ Modo Executor

1. Status da solução  
2. Problemas identificados  
3. Ajustes necessários  
4. Status final (aprovado / revisar)  

---

## 🔄 6. INTEGRAÇÃO COM OUTRAS SKILLS

A skill deve ser combinada conforme necessidade:

---

### 🔗 Combinações comuns

- self_critique + validation → revisão completa
- self_critique + code_generation → melhoria de código
- self_critique + reasoning → revisão de decisão
- self_critique + data_analysis → revisão de insight

---

## ✅ 7. VALIDAÇÃO INTERNA

A skill deve validar:

- a solução atende ao objetivo?
- há erros não identificados?
- há decisões mal justificadas?
- o output pode ser melhorado?

---

## ⚠️ 8. DETECÇÃO DE RISCO

A skill deve identificar:

- inconsistências ocultas
- falhas de raciocínio
- baixa qualidade estrutural
- soluções frágeis ou incompletas

---

### Ação obrigatória:

- destacar problemas claramente
- evitar validação superficial
- impedir aprovação automática

---

## 🧾 9. PADRÕES DE QUALIDADE

A revisão deve:

- ser crítica e objetiva
- evitar viés positivo (não assumir que está correto)
- buscar melhoria real
- garantir consistência com o projeto

---

### ✅ Boas práticas obrigatórias

- questionar a própria solução
- comparar com alternativas possíveis
- revisar antes de finalizar
- evitar validação automática

---

## 🚫 10. PROIBIÇÕES

A skill não deve:

- validar sem analisar profundamente
- ignorar problemas detectados
- aprovar solução incompleta
- evitar apontar falhas
- suavizar erros críticos

---

## 🎯 11. CRITÉRIO DE QUALIDADE

A execução é considerada correta quando:

- a revisão é crítica e estruturada
- problemas reais foram identificados
- melhorias relevantes foram sugeridas
- a solução final é superior à inicial

---

## 🔁 12. RELAÇÃO COM O SISTEMA (agent_rules)

Esta skill suporta diretamente:

- 5.3.3 → revisão da execução
- 6.x → reforço do sistema de avaliação
- validação final antes da entrega

---

## 🚀 13. OBJETIVO FINAL

Garantir que o agente:

- revise suas próprias soluções
- evolua continuamente
- evite regressões
- entregue resultados de alta qualidade