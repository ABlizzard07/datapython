import pandas as pd 
import plotly.express as px

df = pd.read_csv("Coviddata.csv")

figure = px.scatter(df, x = "date", y = "cases", color = "country", size = "cases", size_max = 40)

figure.show()