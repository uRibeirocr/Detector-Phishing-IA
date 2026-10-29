from regras import analisar_url

url = input("Cole a URl: ")
resultado = analisar_url(url)

print("Pontuação de risco:", resultado["pontos"])
for motivo in resultado["motivos"]:
    print("-", motivo)