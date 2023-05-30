import requests
#Para transformar a saída da API em dataframe
#importar as biblioteca de json e pandas conforme abaixo
import pandas as pd
import json
from tqdm import tqdm
url = "https://www.comdinheiro.com.br/Clientes/API/EndPoint001.php"

querystring = {"code":"import_data"}

tickers = ['ABEV3','ALPA4','AMER3','ARZZ3','ASAI3','AZUL4','B3SA3','BBAS3','BBDC3','BBDC4','BBSE3', 'BEEF3','BPAC11', 'BPAN4',
'BRAP4','BRFS3','BRML3','CASH3','CCRO3','CIEL3','CMIG4','CMIN3', 'COGN3','CPFE3','CRFB3','CSAN3','CSNA3','CVCB3','CYRE3','DXCO3','ECOR3','EGIE3', 'ELET3', 'EMBR3', 'ENBR3', 'ENEV3', 'ENGI11', 'EQTL3', 'EZTC3','FLRY3', 'GGBR4', 'GOAU4','GOLL4', 'HAPV3', 'HYPE3', 'IGTI11','IRBR3', 'ITSA4', 'ITUB4','JBSS3','KLBN11',
'LREN3','LWSA3','MGLU3','MRFG3','MRVE3','MULT3','NTCO3','PCAR3','PETR3','PETR4','PETZ3', 'POSI3', 'PRIO3', 'QUAL3', 'RADL3', 'RAIL3', 'RAIZ4', 'RDOR3', 'RENT3',
 'RRRP3', 'SANB11', 'SBSP3', 'SLCE3', 'SMTO3', 'SOMA3', 'SUZB3', 'TAEE11', 'TIMS3', 'TOTS3', 'UGPA3', 'VALE3', 'VBBR3', 'VIIA3', 'VIVT3', 'WEGE3', 'YDUQ3', 'BIDI11',
 'BIDI4', 'GETT11', 'GNDI3', 'JHSF3', 'LAME4', 'LCAM3', 'SULA11', 'BRDT3', 'BTOW3', 'HGTX3', 'IGTA3', 'VVAR3', 'PCAR4', 'SMLS3', 'TIMP3', 'VIVT4', 'ESTC3', 'FIBR3', 'KROT3',
 'LOGG3', 'NATU3', 'BVMF3', 'CTIP3', 'RUMO3', 'SMLE3', 'BRPR3', 'OIBR3', 'TBLE3', 'ALLL3', 'CRUZ3', 'DTEX3',
 'ELPL4', 'EVEN3', 'GFSA3', 'LIGT3', 'OIBR4', 'PDGR3', 'POMO4', 'RLOG3', 'RSID3', 'AEDU3', 'BISA3', 'DASA3',
 'KLBN4', 'LLXL3', 'MMXM3', 'TRPL4', 'USIM3', 'VAGR3', 'AMBV4', 'OGXP3', 'BRTO4', 'RDCD3', 'TAMM4', 'TNLP3', 'TNLP4',
 'BRKM5', 'ECOD3', 'PCAR5', 'PRTX3', 'TCSL3', 'TCSL4', 'TLPP4', 'TMAR5', 'UGPA4','USIM5','VALE5','VIVO4','ALLL11','BRTO3','CGAS5',
'NETC4','BNCA3','BRTP3','BRTP4','DURA4','ITAU4','PRGA3','SDIA4','UBBR11','VCPA4','ACES4','CCPR3','PTIP4','TMCP4','ARCE3','CESP4','CMET4','CTAX3','CTAX4','EBTP4','EMBR4',
'TCOC4','TLCP4','CSTB4','PLIM4','EBTP3','LIGH3','TNEP4']

data_inicio = "02012001"
data_fim = "28042023"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

for i in tqdm(range(len(tickers))):
    ticker = tickers[i]
    payload = f"username=aluno.fernando.zanchitta&password=nifmod-cyjzov-wYnva4&URL=HistoricoCotacaoAcao001-{ticker}-{data_inicio}-{data_fim}-1-1&format=json2"
    try:
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # print(response.text)


    #Acrescentar as seguintes linhas no final do script
    dict = json.loads(response.text)
    df   = pd.DataFrame(dict["resposta"]["tab-p0"]["linha"])
    df.to_csv(f'../data/stocks/{ticker}.csv',index=False)
#Obs.: Sustituir ["chave"] pela chave correspondente