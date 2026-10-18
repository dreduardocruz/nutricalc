"""
Exemplo de integração do seu Pipeline de Bioimpedância (Python / Flask)
com a Calculadora NutriCalc do Instituto Python.
"""
import urllib.parse
import json

def gerar_link_nutricalc(base_url: str, dados_bio: dict) -> str:
    """
    Recebe o dicionário extraído do PDF/App de Bioimpedância e retorna
    a URL pronta para o paciente abrir no iOS / Android com tudo preenchido.
    """
    params = {
        "nome": dados_bio.get("nome", ""),
        "sexo": dados_bio.get("sexo", "F"),
        "idade": dados_bio.get("idade", 35),
        "peso": dados_bio.get("peso", 70.0),
        "altura": dados_bio.get("altura", 165),
        "bf": dados_bio.get("bf", ""),
        "massa_magra": dados_bio.get("massa_magra", ""),
        "tmb": dados_bio.get("tmb", "")
    }
    # Remove chaves vazias
    params = {k: v for k, v in params.items() if v != ""}
    query_string = urllib.parse.urlencode(params)
    return f"{base_url.rstrip('/')}/?{query_string}"

if __name__ == "__main__":
    laudo_exemplo = {
        "nome": "Paciente Exemplo",
        "sexo": "F",
        "idade": 41,
        "peso": 71.4,
        "altura": 163,
        "bf": 24.8,
        "massa_magra": 53.7,
        "tmb": 1530
    }
    url_github_pages = "https://pythonexus.com.br/nutricalc"
    print("Link para enviar ao paciente (WhatsApp / iOS):")
    print(gerar_link_nutricalc(url_github_pages, laudo_exemplo))
    print("\nJSON para colar no modal da calculadora:")
    print(json.dumps(laudo_exemplo, ensure_ascii=False, indent=2))
