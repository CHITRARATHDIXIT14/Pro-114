import csv
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv('data.csv')
data = df['TOEFL'].tolist()
admit = df['Chance'].tolist()

#fig = px.scatter( x=data , y=admit )
#fig.show()

#m = 1
#c = 0
y = []

#for x in data :
   # y_value = m*x + c
   # y.append(y_value)

#Plotting the points
#fig = px.scatter(x=data , y=admit)
#fig.update_layout(shapes=[
    #dict(
    #    type  = 'line',
   #     y0 = min(y) , y1 = max(y),
  #      x0 = min(data) , x1 = max(data)
 #   )
#])

data_array = np.array(data)
admit_array = np.array(admit)

m ,c = np.polyfit(data_array , admit_array , 1)
y = []
for x in data_array:
    y_value = m*x+c
    y.append(y_value)

fig = px.scatter(x=data , y=admit)
fig.update_layout(shapes=[
    dict(
        type  = 'line',
        y0 = min(y) , y1 = max(y),
        x0 = min(data_array) , x1 = max(data_array)
    )
])

fig.show()

x = 250
y = m * x + c
print(f"Chances of admit if the Toefl score {x} is {y}")