from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/api/helo")
def hello():
    '''
    Endpoint de teste para verificar se a API está funcionando corretamente. Retorna uma mensagem de saudação.

    '''
    return {"message": "Hello, World!"}

@app.get("/api/restaurantes/")
def get_restaurantes(restaurante: str= Query(None)):
    '''
    Endpoint para obter informações sobre restaurantes e seus cardápios.
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurantes = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurantes.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurantes}
    else:
        return {'Erro': f'Erro ao fazer a requisição. Código de status: {response.status_code}'}