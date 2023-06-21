import json

import pandas as pd
import requests
from tqdm import tqdm


def get_ibov(datas_de_analise):
    """
    get ibov data using the API from Comdinheiro.

    Concatenate all dataframes in the list

    Example:
        Data de análise: = ['29/12/2022', '29/12/2021', '29/12/2020', '27/12/2019',
       '28/12/2018', '28/12/2017', '28/12/2016', '28/12/2015',
       '29/12/2014', '27/12/2013', '28/12/2012', '29/12/2011',
       '30/12/2010', '30/12/2009', '30/12/2008', '28/12/2007', '28/12/2006',
       '29/12/2005', '30/12/2004', '30/12/2003',"30/12/2002","28/12/2001","27/12/2000"]

    """
    # Create an empty list to store the dataframes
    ibov_list = []

    url = "https://www.comdinheiro.com.br/Clientes/API/EndPoint001.php"

    querystring = {"code": "import_data"}
    for i in tqdm(range(len(datas_de_analise))):
        data = datas_de_analise[i]
        # separar para encaixar no payload: Formato 3D28%2F12%2F2000 para 28/12/2000:
        data = data.replace("/", "%2F")

        # payload = f"username=aluno.fernando.zanchitta&password=nifmod-cyjzov-wYnva4&URL=StockScreenerFull.php%3F%26relat%3D%26data_analise%3D{data}%26data_dem%3D31%2F12%2F9999%26variaveis%3DTICKER%2BNOME_EMPRESA%2Bdata_analise%2BPL%2BQUANT_ON_PN%2BEBIT%2BPRECO%2BAT%2BFATOR_COTACAO%2Bret_12m%2B%2Bret_06m%2Bret_03m%2Bret_01m%2BLC%2Bvol_ano_48m%2Bvol_ano_36m%2Bvol_ano_24m%2Bvol_ano_12m%2Bvol_ano_06m%2Bvol_ano_03m%2Bvol_ano_01m%2BEV%2BMARKET_VALUE%26segmento%3Dtodos%26setor%3Dtodos%26filtro%3DPESO_INDICE%28participacao%2CIBOVESPA%2C%2C30%2C%29%253E0%26demonstracao%3Dconsolidado%2520preferencialmente%26convencao%3DMIXED%26acumular%3D12%26valores_em%3D1%26num_casas%3D2%26salve%3D%26salve_obs%3D%26opcao_salvar%3Dnenhum%26opcao_portfolio%3Dquantidade%26opcao_serie%3Dcash%26indicador_pesos_portfolio%3D%26data_analise_portfolio%3D18%2F04%2F2023%26var_control%3D0%26overwrite%3D0%26setor_bov%3Dtodos%26subsetor_bov%3Dtodos%26subsubsetor_bov%3Dtodos%26group_by%3D%26relat_alias_automatico%3Dcmd_alias_01%26primeira_coluna_ticker%3D0%26periodos%3D22%26periodicidade%3Danual_02%26formato_data%3D1%26tipo_on_pn%3DON%2BPN%2BUNT%26tipo_listagem%3Dlistada_em_bolsa%26casos_especiais_01%3Dnenhum%26casos_especiais_02%3Dapenas_ticke%26pais_origem%3DBR%26exchange%3DB3%26limit_01%3D%26order_by%3D%26moeda%3DMOEDA_ORIGINAL%26nome_serie%3D%26republicacoes%3D0%26linppag%3D50&format=json2"
        payload = f"username=aluno.fernando.zanchitta&password=nifmod-cyjzov-wYnva4&URL=StockScreenerFull.php%3F%26relat%3D%26data_analise%3D{data}%26data_dem%3D31%2F12%2F9999%26variaveis%3DTICKER%2BNOME_EMPRESA%2Bdata_analise%2BPL%2BQUANT_ON_PN%2BEBIT%2BPRECO%2BAT%2BFATOR_COTACAO%2Bret_12m%2Bret_06m%2Bret_03m%2Bret_01m%2BLC%2Bvol_ano_12m%2Bvol_ano_06m%2Bvol_ano_03m%2Bvol_ano_01m%2BEV%2BMARKET_VALUE%26segmento%3Dtodos%26setor%3Dtodos%26filtro%3DPESO_INDICE%28participacao%2CIBOVESPA%2C%2C30%2C%29%253E0%26demonstracao%3Dconsolidado%2520preferencialmente%26convencao%3DMIXED%26acumular%3D12%26valores_em%3D1%26num_casas%3D2%26salve%3D%26salve_obs%3D%26opcao_salvar%3Dnenhum%26opcao_portfolio%3Dquantidade%26opcao_serie%3Dcash%26indicador_pesos_portfolio%3D%26data_analise_portfolio%3D18%2F04%2F2023%26var_control%3D0%26overwrite%3D0%26setor_bov%3Dtodos%26subsetor_bov%3Dtodos%26subsubsetor_bov%3Dtodos%26group_by%3D%26relat_alias_automatico%3Dcmd_alias_01%26primeira_coluna_ticker%3D0%26periodos%3D0%26periodicidade%3Danual_02%26formato_data%3D1%26tipo_on_pn%3DON%2BPN%2BUNT%26tipo_listagem%3Dlistada_em_bolsa%26casos_especiais_01%3Dnenhum%26casos_especiais_02%3Dapenas_ticke%26pais_origem%3DBR%26exchange%3DB3%26limit_01%3D%26order_by%3D%26moeda%3DMOEDA_ORIGINAL%26nome_serie%3D%26republicacoes%3D0%26linppag%3D50&format=json2"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        try:
            response = requests.request(
                "POST",
                url,
                data=payload,
                headers=headers,
                params=querystring,
            )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        dict = json.loads(response.text)
        print(response.text)
        ibov_this_date = pd.DataFrame(dict["resposta"]["tab-p0"]["linha"])
        ibov_list.append(ibov_this_date)

    # Concatenate all dataframes in the list
    ibov = pd.concat(ibov_list, axis=0)
    # Save the dataframe as a csv file
    ibov.to_csv("../data/ibov_universe.csv", index=False)
    return ibov


def get_one_stock(ticker, data_inicio, data_fim):
    """
     get data from one stock using the API from Comdinheiro.

     Example:
        ticker = "ITUB3"
        data_inicio = "02012001"
        data_fim = "28042023"

    """
    url = "https://www.comdinheiro.com.br/Clientes/API/EndPoint001.php"

    querystring = {"code": "import_data"}
    payload = f"username=aluno.fernando.zanchitta&password=nifmod-cyjzov-wYnva4&URL=HistoricoCotacaoAcao001-{ticker}-{data_inicio}-{data_fim}-1-1&format=json2"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    try:
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            params=querystring,
        )
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # print(response.text)
    dict = json.loads(response.text)
    df = pd.DataFrame(dict["resposta"]["tab-p0"]["linha"])
    df.to_csv(f"../../data/stocks/{ticker}.csv", index=False)
    # Obs.: Sustituir ["chave"] pela chave correspondente
    return df


def get_multiple_stocks(tickers, data_inicio, data_fim):
    """

    get data from multiple stocks using the API from Comdinheiro.

    Example:
        tickers = [
            'ABEV3','ALPA4','AMER3','ARZZ3','ASAI3','AZUL4','B3SA3','BBAS3','BBDC3','BBDC4','BBSE3', 'BEEF3','BPAC11', 'BPAN4',
            'BRAP4','BRFS3','BRML3','CASH3','CCRO3','CIEL3','CMIG4','CMIN3', 'COGN3','CPFE3','CRFB3','CSAN3','CSNA3','CVCB3',
            'CYRE3','DXCO3','ECOR3','EGIE3', 'ELET3', 'EMBR3', 'ENBR3', 'ENEV3', 'ENGI11', 'EQTL3', 'EZTC3','FLRY3', 'GGBR4', 
            'GOAU4','GOLL4', 'HAPV3', 'HYPE3', 'IGTI11','IRBR3', 'ITSA4', 'ITUB4','JBSS3','KLBN11','LREN3','LWSA3','MGLU3',
            'MRFG3','MRVE3','MULT3','NTCO3','PCAR3','PETR3','PETR4','PETZ3', 'POSI3', 'PRIO3', 'QUAL3', 'RADL3', 'RAIL3', 
            'RAIZ4', 'RDOR3', 'RENT3','RRRP3', 'SANB11', 'SBSP3', 'SLCE3', 'SMTO3', 'SOMA3', 'SUZB3', 'TAEE11', 'TIMS3', 
            'TOTS3', 'UGPA3', 'VALE3', 'VBBR3', 'VIIA3', 'VIVT3', 'WEGE3', 'YDUQ3', 'BIDI11','BIDI4', 'GETT11', 'GNDI3', 
            'JHSF3', 'LAME4', 'LCAM3', 'SULA11', 'BRDT3', 'BTOW3', 'HGTX3', 'IGTA3', 'VVAR3', 'PCAR4', 'SMLS3', 'TIMP3', 
            'VIVT4', 'ESTC3', 'FIBR3', 'KROT3','LOGG3', 'NATU3', 'BVMF3', 'CTIP3', 'RUMO3', 'SMLE3', 'BRPR3', 'OIBR3', 
            'TBLE3', 'ALLL3', 'CRUZ3', 'DTEX3','ELPL4', 'EVEN3', 'GFSA3', 'LIGT3', 'OIBR4', 'PDGR3', 'POMO4', 'RLOG3',
            'RSID3', 'AEDU3', 'BISA3', 'DASA3','KLBN4', 'LLXL3', 'MMXM3', 'TRPL4', 'USIM3', 'VAGR3', 'AMBV4', 'OGXP3',
            'BRTO4', 'RDCD3', 'TAMM4', 'TNLP3', 'TNLP4','BRKM5', 'ECOD3', 'PCAR5', 'PRTX3', 'TCSL3', 'TCSL4', 'TLPP4',
            'TMAR5', 'UGPA4','USIM5','VALE5','VIVO4','ALLL11','BRTO3','CGAS5','NETC4','BNCA3','BRTP3','BRTP4','DURA4',
            'ITAU4','PRGA3','SDIA4','UBBR11','VCPA4','ACES4','CCPR3','PTIP4','TMCP4','ARCE3','CESP4','CMET4','CTAX3',
            'CTAX4','EBTP4','EMBR4','TCOC4','TLCP4','CSTB4','PLIM4','EBTP3','LIGH3','TNEP4']
        data_inicio = "02012001"
        data_fim = "28042023"
    """
    url = "https://www.comdinheiro.com.br/Clientes/API/EndPoint001.php"

    querystring = {"code": "import_data"}

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    for i in tqdm(range(len(tickers))):
        ticker = tickers[i]
        payload = f"username=aluno.fernando.zanchitta&password=nifmod-cyjzov-wYnva4&URL=HistoricoCotacaoAcao001-{ticker}-{data_inicio}-{data_fim}-1-1&format=json2"
        try:
            response = requests.request(
                "POST",
                url,
                data=payload,
                headers=headers,
                params=querystring,
            )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        # print(response.text)

        # Acrescentar as seguintes linhas no final do script
    dict = json.loads(response.text)
    df = pd.DataFrame(dict["resposta"]["tab-p0"]["linha"])
    df.to_csv(f"../../data/stocks/{ticker}.csv", index=False)
    # Obs.: Sustituir ["chave"] pela chave correspondente
    return df



# import requests

# url = "https://www.comdinheiro.com.br/Clientes/API/EndPoint001.php"

# querystring = {"code":"import_data"}


# headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

# print(response.text)

# #Para transformar a saída da API em dataframe
# #importar as biblioteca de json e pandas conforme abaixo
# #import pandas as pd
# #import json
# #Acrescentar as seguintes linhas no final do script
# #dict = json.loads(response.text)
# #df   = pd.DataFrame(dict["chave"])
# #Obs.: Sustituir ["chave"] pela chave correspondente