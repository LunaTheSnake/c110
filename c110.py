import pandas as pd
import plotly.figure_factory as ff
import statistics
import csv

df= pd.read_csv("Avg.csv")

data= df["average"]

fig= ff.create_distplot([data], ["average"])

fig.show()
