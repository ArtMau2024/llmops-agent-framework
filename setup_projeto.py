import os

#Nome da pasta raiz
root = "projeto_llmops"

# Estrutura de pastas
folders = [
    "01_Contexto",
    "02_specs",
    "03_agent_config",
    "04_execucao/codigo",
    "04_execucao/dados",
    "05_evaluation"
]
#Criar pasta raiz
os.makedirs(root, exist_ok=True)


# Criar subpastas
for folder in folders:
    path = os.path.join(root, folder)
    os.makedirs(path, exist_ok=True)

print("✅ Estrutura do projeto criada com sucesso!")
files = [
    "01_contexto/projeto_master.md",
    "03_agent_config/agent_rules.md",
    "03_agent_config/skills.md",
    "05_evaluation/criterios.md"
]

for file in files:
    file_path = os.path.join(root, file)
    
    # cria arquivo vazio se não existir
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("# " + file.split("/")[-1].replace(".md", "").upper())

print("✅ Arquivos base criados!")