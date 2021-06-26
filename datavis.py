import pandas as pd 
import plotly.express as px
import statistics
import csv

df = pd.read_csv("visual.csv")
group = df.groupby(['student_id','level'], as_index = False)['attempt'].mean()

fig = px.scatter(group,
 x = 'student_id',
 y = 'level')

fig.show()