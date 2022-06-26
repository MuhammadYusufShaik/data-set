import pandas as pd

import plotly.figure_factory as pf
import random 
import statistics as st
df=pd.read_csv('C:/Users/khada/Downloads/python/c110/newdata.csv')
average=df['average'].tolist()

finaldata=[]
def samplen():
    data=[]
    for i in range(0,100):
        pos=random.randint(0,len(average)-1)
        data.append(average[pos])
    mean=st.mean(data)
    finaldata.append(mean)
for i in range(0,1000):
    samplen()
graph=pf.create_distplot([finaldata],['average graph'],show_hist=False)
graph.show()