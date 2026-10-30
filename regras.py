import re 
from urllib.parse import urlparse
from marcas import MARCAS

PALAVRAS_SUSPEITAS = ["verificar","conta","senha","urgente","login", "atualizar", "bloqueada", "confirmar"]

def analisar_url(url: str) -> dict:
    pontos = 0
    motivos = []

    if "://" not in url:
        url = "http://" + url

    dominio = urlparse(url).netloc.lower()
#regra 1
    if len(url) > 75:
        pontos += 1
        motivos.append("URL muito longa")
#regra 2
    if re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}(:\d+)?",dominio):
        pontos += 3
        motivos.append("Usa endereço IP em vez de domínio")
#regra 3
    if dominio.count(".") >= 4:
        pontos += 2
        motivos.append("Muitos subdomínios")
#regra 4
    encontradas = []
    for p in PALAVRAS_SUSPEITAS:
        if p in url.lower():
            encontradas.append(p)
        
    if encontradas:
        pontos += len(encontradas)
        motivos.append(f"Palavras suspeitas: {', '.join(encontradas)}")
#regra 5

    if not url.startswith("https://"):
        pontos += 1
        motivos.append("Não usa HTTPS")
#regra 6
    if "@" in url:
        pontos += 2
        motivos.append("Contém '@' na URL")
#regra 7
    for marca, oficial in MARCAS.items():
        if marca in dominio:
            e_oficial = dominio == oficial or dominio.endswith("." + oficial)
            if not e_oficial:
                pontos += 3
                motivos.append(f"Imita a marca '{marca}', mas nao é o site oficial")

    return {"pontos": pontos, "motivos": motivos}



