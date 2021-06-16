import plotly.express as px
import csv
import numpy as np
with open("correlation_s.csv")as csv_file:
   df=csv.DictReader(csv_file)
   fig=px.scatter(df,x="Marks In Percentage", y="Days Present")
   fig.show()
def getDataSource(data_path):
   mark_data=[]
   present_data=[]
   with open(data_path)as csv_file:
      csv_reader=csv.DictReader(csv_file)
      for row in csv_reader:
         mark_data.append(float(row["Marks In Percentage"]))
         present_data.append(float(row["Days Present"]))
   return{"x":mark_data,"y":present_data}
def findCorrelation(dataSource):
   correlation=np.corrcoef(dataSource["x"],dataSource["y"])
   print("Correlation is ->",correlation[0,1])
def setup():
   data_path="correlation_s.csv"
   dataSource=getDataSource(data_path)
   findCorrelation(dataSource)
setup()