import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

meses=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

inv_range = [5,6,7,8]
ver_range = [11, 12, 1, 2, 3]

def month_name(month):
    return meses[month-1]

def month_number(month):
    return meses.index(month)+1

def df_invierno(df, i_year, f_year):
    invierno = pd.DataFrame()
    for year in range(i_year, f_year+1):
        i = datetime(year, 5, 1, 0, 0)
        f = datetime(year, 8, 31, 23, 0)
        frame = [invierno,df.loc[i:f]]
        invierno = pd.concat(frame)
    return invierno

def gpr_invierno(date):
    return date.year

def df_verano(df, i_year, f_year):
    verano = pd.DataFrame()
    for year in range(i_year, f_year+1):
        i = datetime(year, 11, 1, 0, 0)
        f = datetime(year+1, 3, 31, 23, 0)
        frame = [verano,df.loc[i:f]]
        verano = pd.concat(frame)
    return verano

def gpr_verano(date):
    if date.month >= 11:
        return date.year
    else:
        return date.year-1

def o3delta(df, delta):
    if delta == 0:
        return df
    df = df.reset_index()
    dfr = df['O3']
    dfl = df.drop(columns='O3')
    dfr = dfr.iloc[delta:].reset_index(drop=True)
    dfl = dfl.iloc[:-delta].reset_index(drop=True)
    df = pd.concat([dfl, dfr], axis=1)
    df.set_index('registered_on')
    return df


#def gpr_month(date):
#    return month_name(date.month)

#def gpr_year_month(date):
#    year = str(date.year)
#    month = month_name(date.month)
#    return year+" "+month

#def boxplot_by_month(gpi):
#    gg = gpi.get_group(2010)[['NO']]
#    gg['month'] = gg.index.to_frame().agg(lambda x:x.index.month)
#    hh = pd.DataFrame()
#    hh = pd.concat([hh.reset_index().drop('index', axis=1), gg[gg['month']==5].reset_index()['NO']], ignore_index=True, axis=1)
#    hh.describe()
#    hh = pd.concat([hh.reset_index().drop('index', axis=1), gg[gg['month']==6].reset_index()['NO']], ignore_index=True, axis=1)
#    #hh.describe()
#    hh = pd.concat([hh.reset_index().drop('index', axis=1), gg[gg['month']==7].reset_index()['NO']], ignore_index=True, axis=1)
#    hh = pd.concat([hh.reset_index().drop('index', axis=1), gg[gg['month']==8].reset_index()['NO']], ignore_index=True, axis=1)
#    
#    hh.columns = [5,6,7,8]
#    #hh
#    hh.iplot(kind='box', boxpoints = 'outliers' )
#
#def boxplot_all(df, predictor):
#    df = df[[predictor]]
#    group = df.groupby(by=gpr_year_month, sort=False)
#    group.boxplot(subplots=False, figsize=(100,2))
#    plt.show()