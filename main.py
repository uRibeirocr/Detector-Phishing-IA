from regras import analisar_url
from banco import criar_banco

criar_banco()

url = input("Cole a URl: ")
resultado = analisar_url(url)

print("Pontuação de risco:", resultado["pontos"])
for motivo in resultado["motivos"]:
    print("-", motivo)