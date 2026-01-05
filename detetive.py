import os

pasta = r"C:\Users\DEMOTTA\Documents\PROJETOS PYTHON"

print(f"--- ARQUIVOS NA PASTA: {pasta} ---")

if os.path.exists(pasta):
    arquivos = os.listdir(pasta)
    for arquivo in arquivos:
        print(f"📄 {arquivo}")
else:
    print("❌ A pasta informada não existe.")