import pandas as pd
import numpy as np
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

def choose_stock(ticker):
    """
    input:str,str
    read and store ticker information.
    'data': Date in format: 'dd/mm/yyyy',
    'fech_ajustado': Close price adjusted for splits and dividends,
    'variacao(pct)': Daily return in percentage,
    'fech_historico': Close price without adjustments,
    'abertura_ajustado': Open price adjusted for splits and dividends,
    'min_ajustado': Low price adjusted for splits and dividends, 
    'medio_ajustado': Average price adjusted for splits and dividends, 
    'max_ajustado': High price adjusted for splits and dividends,
    'vol_(mm_r$)': Volume in millions of R$, 
    'negocios': Number of trades, 
    'fator': Factor, 
    'tipo': Type (PN, ON, etc), 
    'quant_em_aluguel': Number of shares in short position,
    'vol_em_aluguel(mm_r$)': Volume in millions of R$ in short position,
    output:dataframe
    """
    stock = pd.read_csv(f"../data/stocks/{ticker}.csv", index_col = None)
    # Convert datetime column to desired format
    print(stock.columns)
    stock = stock.rename(columns={'data': 'date'})
    stock['date'] = pd.to_datetime(stock['date'], format="%d/%m/%Y")
    stock["date"] = stock["date"].dt.strftime("%Y/%m/%d")
    # transform all nd to NaN:
    stock = stock.replace('nd', np.nan)
    # all columns to float64, except date and type:
    columns_to_convert = ["fech_ajustado", "variacao(pct)", "fech_historico", "abertura_ajustado","min_ajustado","medio_ajustado", "max_ajustado", "vol_(mm_r$)", "negocios", "fator", "quant_em_aluguel","vol_em_aluguel(mm_r$)"]
    stock[columns_to_convert] = stock[columns_to_convert].replace(',', '.', regex=True)
    stock[columns_to_convert] = stock[columns_to_convert].astype(float)
    stock.set_index('date', inplace = True)
    return stock
def process_stock(frame):
        """
        Process the stock dataframe to be ready to be consumed.
        input:dataframe
        output:dataframe
        """
        # Selecting columns to keep:
        column_to_keep = ['fech_ajustado','variacao(pct)']
        frame = frame.loc[:, column_to_keep]
        # Renaming to Close and Returns:
        frame = frame.rename(columns={'fech_ajustado': 'Close', 'variacao(pct)': 'Returns'})
        # dropna:
        frame = frame.dropna()
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

def split_data(data,rate=0.8):
    """
    input: dataframe, float
    Split the data into training and testing datasets.
    When using time series data, it is important to split the data as follows:
    output: X_train, X_test, y_train, y_test,close_test
    """
    # Define X and y variables:
    X = data.drop('Returns', axis=1)
    X = X.drop('Close',axis=1)
    y = data.loc[:, 'Returns']
    # Split into Training/Testing Data:
    split = int(rate * len(X))
    X_train = X[: split]
    X_test = X[split:]
    y_train = y[: split]
    y_test = y[split:]
    close_test=data["Close"][split:]
    close_test
    return X_train, X_test, y_train, y_test,close_test
