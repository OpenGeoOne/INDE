import requests

url = "https://www.inde.gov.br/api/catalogo/get"
response = requests.get(url, verify=False)

if response.status_code == 200:
    dados = response.json()
    for item in dados:
        print(item['descricao'])
        print(dados[0].keys())
else:
    print("Erro:", response.status_code)
