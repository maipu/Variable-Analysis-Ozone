import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import utils
from utils import gpr_invierno, gpr_verano

#anyos 1997 hasta 2017
#veranor
#invierno

##def df_invierno(df, i_year, f_year):
##    invierno = pd.DataFrame()
##    for year in range(i_year, f_year+1):
##        i = datetime(year, 5, 1, 0, 0)
##        f = datetime(year, 8, 31, 23, 0)
##        frame = [invierno,df.loc[i:f]]
##        invierno = pd.concat(frame)
##    return invierno
##
##def gpr_invierno(date):
##    return date.year
##
##def df_verano(df, i_year, f_year):
##    verano = pd.DataFrame()
##    for year in range(i_year, f_year):
##        i = datetime(year, 11, 1, 0, 0)
##        f = datetime(year+1, 3, 31, 23, 0)
##        frame = [verano,df.loc[i:f]]
##        verano = pd.concat(frame)
##    return verano
##
##def gpr_verano(date):
##    if date.month >= 11:
##        return date.year
##    else:
##        return date.year-1
##
##def gpr_month(date):
##    meses=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
##    #meses = [1,2,3,4,5,6,7,8,9,10,11,12]
##    return meses[date.month-1]
##
##def plot_by_month(dfg, year, predictor):
##    df = dfg.get_group(year)[[predictor]]
##    group = df.groupby(by=gpr_month, sort=False)
##    ax=group.boxplot(subplots=False)
##    fig = ax.get_figure()
##    fig.suptitle(str(year))
##    plt.show()


ozone = pd.read_hdf("datasets/dump-Las_Condes_2018-04-12_230000.h5","table")

invierno = utils.df_invierno(ozone, 1997, 2017)
verano = utils.df_verano(ozone, 1997, 2017)

gpi = invierno.groupby(by=gpr_invierno)
gpv = verano.groupby(by=gpr_verano)

#utils.boxplot_by_month(gpi, 2010, 'O3')
#utils.boxplot_by_month(gpv,2010,'O3')


utils.boxplot_all(gpi.filter(lambda x:True), 'O3')

#df_NO = gpi.get_group(2010)[['NO']]
#
#group = df_NO.groupby(by=gpr_month, sort=False)
#
#group.boxplot(subplots=False)
#
#plt.show()