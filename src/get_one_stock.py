import requests

url = "https://www.comdinheiro.com.br/Clientes/API/EndPoint001.php"

querystring = {"code":"import_data"}
ticker = "ITUB3"
data_inicio = "02012001"
data_fim = "28042023"
payload = f"username=aluno.fernando.zanchitta&password=nifmod-cyjzov-wYnva4&URL=HistoricoCotacaoAcao001-{ticker}-{data_inicio}-{data_fim}-1-1&format=json2"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

try:
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
# print(response.text)

#Para transformar a saída da API em dataframe
#importar as biblioteca de json e pandas conforme abaixo
import pandas as pd
import json
#Acrescentar as seguintes linhas no final do script
dict = json.loads(response.text)
df   = pd.DataFrame(dict["resposta"]["tab-p0"]["linha"])
df.to_csv(f'../data/stocks/{ticker}.csv',index=False)
#Obs.: Sustituir ["chave"] pela chave correspondente