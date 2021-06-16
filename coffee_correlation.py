import plotly.express as px
import csv
import numpy as np
with open("correlation_c.csv")as csv_file:
   df=csv.DictReader(csv_file)
   fig=px.scatter(df,x="Coffee in ml", y="sleep in hours")
   fig.show()
def getDataSource(data_path):
   coffee_data=[]
def getDataSource(data_path):
   coffee_data=[]
   sleep_data=[]
   with open(data_path)as csv_file:
      csv_reader=csv.DictReader(csv_file)
      for row in csv_reader:
         coffee_data.append(float(row["Coffee in ml"]))
         sleep_data.append(float(row["sleep in hours"]))
   return{"x":coffee_data,"y":sleep_data}
def findCorrelation(dataSource):
   correlation=np.corrcoef(dataSource["x"],dataSource["y"])
   print("Correlation is ->",correlation[0,1])
def setup():
   data_path="correlation_c.csv"
   dataSource=getDataSource(data_path)
   findCorrelation(dataSource)
setup()