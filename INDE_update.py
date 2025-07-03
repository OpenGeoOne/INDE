import requests

url = "https://www.inde.gov.br/api/catalogo/get"
response = requests.get(url, verify=False)
InstLista = []
renomear = {'SEFIN - Secretaria Municipal das Finanças de Fortaleza (CE)': 'SEFIN (CE)',
            'FMADS - Fundação Municipal do Meio Ambiente e Desenvolvimento Sustentável de São José (SC)': 'FMADS (SC)',
            'SEFAZ - Secretaria Municipal da Fazenda de Salvador (BA)': 'SEFAZ (BA)',
            'SEFIN - Secretaria Municipal das Finanças de Fortaleza (CE)': 'SEFIN (CE)',
            'PRODATER - Empresa Teresinense de Processamento de Dados (PI)': 'PRODATER (PI)',
            'Prefeitura do Município de São Paulo (SP) - vetor': 'Prefeitura do Município de São Paulo (SP) "vetor"',
            'Prefeitura do Município de São Paulo (SP) - raster': 'Prefeitura do Município de São Paulo (SP) raster',
            'IDE-GEOBASES  (ES) - Sistema Integrado de Bases Geoespaciais do Estado do Espírito Santo ': 'IDE-GEOBASES (ES)',
            'TCE-RO - Tribunal de Contas do Estado de Rondônia': 'TCE (RO)',
            }
InstDic = {}
if response.status_code == 200:
    dados = response.json()
    for k, item in enumerate(dados):
        nome = item['descricao']
        if nome in renomear:
            nome = renomear[nome]
        else:
            nome = nome.split('-')[0].strip()
        nome = nome.replace(r'/','_')
        print(k+1, nome)
        InstLista.append(nome)
        InstDic[nome] = {'url': item['url'],
                         'wmsAvailable': item['wmsAvailable'],
                         'wfsAvailable': item['wfsAvailable'],
                         'wcsAvailable': item['wcsAvailable'],
                        }
else:
    print("Erro:", response.status_code)