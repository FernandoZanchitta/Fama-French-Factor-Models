import pandas as pd
def pre_processing(df):
    """
    input: dataframe
    Steps made before the data is ready to be consumed. 
    No calculation or transformation is made.
    output:dateframe
    """
    # Convert the "year," "month," and "date" columns to datetime format
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])

    # Format the "date" column to the desired format
    df['date'] = df['date'].dt.strftime("%Y/%m/%d")
    df = df.drop(['year', 'month', 'day'],axis=1)
    df.set_index('date', inplace = True)
    return df

def choose_stock(ticker,location):
    """
    input:str,str
    read and store ticker information.
    output:dataframe
    """
    ticker_file=ticker+".xlsx"
    stock = pd.read_excel(location+"/"+ticker_file, index_col = None)
    # Convert datetime column to desired format
    print(stock.columns)
    stock = stock.rename(columns={'Data': 'date'})
    stock["date"] = stock["date"].dt.strftime("%Y/%m/%d")
    stock.set_index('date', inplace = True)
    return stock

def prepare_portfolio(frame,is_stock):
    if is_stock:
        """
        ['Fech Ajustado', 'Variação(%)', 'Fech Histórico', 'Abertura Ajustado',
       'Mín Ajustado', 'Médio Ajustado', 'Máx Ajustado', 'Vol (MM R$)',
       'Negócios', 'Fator', 'Tipo']
        """
        column_to_keep = ['Fech Ajustado','Variação(%)']
        frame = frame.loc[:, column_to_keep]
        frame = frame[~frame.apply(lambda row: row.astype(str).str.contains('nd')).any(axis=1)]
        frame['Close'] = frame['Fech Ajustado'].astype(float)
        frame['Returns'] = frame['Variação(%)'].astype(float)
        frame = frame.drop(columns=column_to_keep)
        #     stock = pd.read_excel(location+"/"+ticker_file, index_col='Date', parse_dates=True,infer_datetime_format=True)
#         frame["Returns"]=frame["Close"].dropna().pct_change()*100
        #     stock.index = pd.Series(stock.index).dt.date
        return frame
    else:
        return frame
    
def analyse_stock(df):
    """
    input: Dataframe
    output:None, Stdout: Multiple Plots
    """
    sns.lineplot(data = df, x = 'Data', y = 'Returns')

    
def merge_portifolio(portfolio,factors):
    """
    input: dataframe,dataframe
    Generate a single portfolio that contains all Factors columns
    in addiction to the portfolio value weighted returns
    output: dataframe
    """
    combined_df = pd.concat([factors, portfolio], axis='columns', join='inner')
    combined_df = combined_df.dropna()
    combined_df = combined_df.drop('Risk_free', axis=1)
    combined_df = combined_df.rename(columns={'Rm_minus_Rf': 'Mkt-RF'})
    return combined_df
def portfolio_build(): 
    pass

