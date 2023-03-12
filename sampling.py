import pandas as pd
import plotly.figure_factory as ff
import statistics
import csv
import random
import plotly.graph_objects as go

df= pd.read_csv("Avg.csv")

data= df["average"]

def random_set(counter):
    dataset = []
    for i in range(0,counter):
        index = random.randint(0,len(data)-1)
        value = data[index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_figure(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["average"])
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines"))

    fig.show()

def setup():
    meanlist = []
    for i in range(0,1000):
        setofmean = random_set(100)
        meanlist.append(setofmean)
    
    show_figure(meanlist)

setup()

def std_deviation():
    meanlist = []
    for i in range(0,1000):
        setofmean = random_set(100)
        meanlist.append(setofmean)
    std =  statistics.stdev(meanlist)

    print("stander deviation = ", std)

std_deviation()

population_mean = statistics.mean(data)

print("mean =",population_mean)
