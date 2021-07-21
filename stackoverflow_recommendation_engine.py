import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plot

#To get the absolute path
def get_absolute_value(val):
    value=int(np.round(val/100*topKeywords.sum(),0))
    return value

#Read CSV file
workingDir=os.path.dirname(os.path.realpath(__file__))
csvPath=workingDir + "/MLTollsStackOverflow.csv"
csvReader=pd.read_csv(csvPath,index_col=0)

#print(csvReader)
print(csvReader.isnull().sum())

#To display number of rows in each column
print(csvReader.count(axis=0))

#Get column headers
columnHeaders=csvReader.columns
print(columnHeaders)

#To get the count of keywords and sort it in descending order
keywordsCount=csvReader.sum(axis=0)
topKeywords=keywordsCount.sort_values(ascending=False)[0:3]

#Plot a piechart that has the top 3 keywords along with the number of times the keyword is searched
plot.pie(topKeywords,labels=topKeywords.index,radius=1,autopct=get_absolute_value)
plot.title("Top 3 most searched keywords on StackOverflow")
plot.show()
