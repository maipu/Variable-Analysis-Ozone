import pandas as pd
import utils
import sys

since = 1997
until = 2017



name = sys.argv[1]

ozone = pd.read_hdf(name,"table")

invierno = utils.df_invierno(ozone, since, until)
verano = utils.df_verano(ozone, since, until)


invierno.to_csv(name[:-3] + "-invierno.csv", na_rep='NaN')
verano.to_csv(name[:-3] + "-verano.csv", na_rep='NaN')