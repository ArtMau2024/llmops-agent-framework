# ✅ SKILL — VALIDATION (Validação Técnica e de Dados)

---

## 🎯 1. OBJETIVO DA SKILL

A skill de validation é responsável por garantir a qualidade, confiabilidade e segurança das soluções geradas pelo agente.

Seu objetivo é:

- verificar se a solução está correta
- garantir consistência lógica e técnica
- validar dados e cálculos
- evitar erros em produção
- impedir entrega de resultados não confiáveis

---

## 🧠 2. QUANDO UTILIZAR

Esta skill deve ser ativada quando houver:

- finalização de uma solução
- geração de código
- análise de dados
- tomada de decisão baseada em dados
- necessidade de validar outputs

---

## 📊 3. PAPEL NO SISTEMA

A skill de validation pode atuar como:

---

### ✅ Skill principal

Quando o objetivo for:

- validar uma solução existente
- verificar consistência de dados
- revisar outputs
- realizar auditoria técnica

---

### ✅ Skill de suporte

Combinada com:

- code_generation → validar código gerado
- data_analysis → validar cálculos e interpretação
- reasoning → validar coerência lógica

---

## ⚙️ 4. LÓGICA DE EXECUÇÃO

A execução deve seguir obrigatoriamente:

---

### 1. Identificação do objeto de validação

- identificar o que está sendo validado
  (código, análise, lógica, resultado)
- compreender o objetivo da solução

---

### 2. Validação lógica

- verificar se a solução faz sentido
- identificar inconsistências
- avaliar coerência com o problema

---

### 3. Validação de dados

- verificar integridade dos dados
- confirmar cálculos
- garantir consistência de valores

---

### 4. Validação de execução

- avaliar se o código funciona
- verificar dependências
- identificar possíveis falhas

---

### 5. Validação de aderência ao projeto

- verificar alinhamento com o agent_rules
- confirmar aderência aos MVPs
- validar compatibilidade com soluções existentes

---

### 6. Conclusão da validação

- classificar a solução (válida / parcialmente válida / inválida)
- indicar ajustes necessários
- apontar riscos remanescentes

---

## 🧩 5. ESTRUTURA DE RESPOSTA

---

### 📘 Modo Mentor

1. Objeto da validação  
2. Critérios utilizados  
3. Análise detalhada  
4. Problemas encontrados  
5. Recomendações  

---

### ⚙️ Modo Executor

1. Status da validação  
2. Problemas críticos  
3. Ajustes necessários  
4. Próxima ação  

---

## 🔄 6. INTEGRAÇÃO COM OUTRAS SKILLS

A skill deve ser combinada conforme necessidade:

---

### 🔗 Combinações comuns

- validation + code_generation → garantir qualidade do código
- validation + data_analysis → validar resultados
- validation + reasoning → validar decisões
- validation + self_critique → revisão completa

---

## ✅ 7. VALIDAÇÃO INTERNA

A skill deve validar:

- a solução está correta?
- os dados são confiáveis?
- há inconsistências?
- a solução pode ser executada?

---

## ⚠️ 8. DETECÇÃO DE RISCO

A skill deve identificar:

- dados inválidos ou incompletos
- lógica inconsistente
- resultados incoerentes
- dependências não tratadas

---

### Ação obrigatória:

- classificar o risco (baixo, médio, alto)
- explicitar o problema
- impedir conclusão indevida

---

## 🧾 9. PADRÕES DE QUALIDADE

A validação deve garantir:

- precisão nos resultados
- clareza da solução
- consistência lógica
- rastreabilidade completa

---

### ✅ Boas práticas obrigatórias

- validar antes, durante e após execução
- revisar premissas utilizadas
- evitar aprovação automática
- justificar conclusões

---

## 🚫 10. PROIBIÇÕES

A skill não deve:

- validar sem verificar lógica
- aprovar soluções incompletas
- ignorar inconsistências
- aceitar dados não confiáveis
- permitir entrega de solução com risco não tratado

---

## 🎯 11. CRITÉRIO DE QUALIDADE

A execução é considerada correta quando:

- a solução foi completamente validada
- não há inconsistências relevantes
- a execução é segura
- a solução pode ser utilizada em produção

---

## 🔁 12. RELAÇÃO COM O SISTEMA (agent_rules)

Esta skill suporta diretamente:

- 5.3.2 → validação da combinação de skills
- 5.3.3 → validação durante execução
- 6.x → sistema completo de avaliação

---

## 🚀 13. OBJETIVO FINAL

Garantir que o agente:

- não entregue soluções erradas
- mantenha alto padrão de qualidade
- suporte decisões confiáveis
- funcione como um sistema auditável