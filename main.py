from duckduckgo_search import DDGS
import json

def buscar_vitrine(query):
    print(f"Buscando por: {query}...")
    ddgs = DDGS()
    
    # Busca texto e imagens com SafeSearch desligado (+18 permitido)
    resultados_links = list(ddgs.text(query, safesearch='off', max_results=5))
    resultados_imagens = list(ddgs.images(query, safesearch='off', max_results=5))
    
    vitrine = {
        "links": [{"titulo": r['title'], "url": r['href']} for r in resultados_links],
        "imagens": [img['image'] for img in resultados_imagens]
    }
    
    return vitrine

if __name__ == "__main__":
    busca = input("Digite a pesquisa: ")
    dados = buscar_vitrine(busca)
    print("\n--- RESULTADOS DA VITRINE ---")
    print(json.dumps(dados, indent=2, ensure_ascii=False))
