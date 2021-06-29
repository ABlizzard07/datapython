import pandas as pd
import csv
import plotly.figure_factory as ff

reader = pd.read_csv('phonerating.csv')

fig = ff.create_distplot([reader['Avg Rating'].tolist()], ['Rating'], show_hist = True)
fig.show()
