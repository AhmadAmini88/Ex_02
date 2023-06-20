#import the packages 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from age import age
from sex import sex
from cp import cp
from ecdf import ecdf

 

#import the data
data = pd.read_csv('dataset.csv')

#analize The age data
age(data)

#Analyze sex data 
sex(data)

#Analyze cp data 
cp(data)


# Empirical cumulative distribution function
ecdf(data)

#Analyze cp data and Plotting a histogram
rbp_data = data['trestbps']
print("Total Blood Pressure Data")
print("Minimum BP:"+str(min(rbp_data)))
print("Maximum BP:"+str(max(rbp_data)))
print("Average BP:"+str(np.mean(rbp_data)))
print("Median BP:"+str(np.median(rbp_data)))
plt.figure(4)
plt.hist(rbp_data, bins=8)
plt.title('Total Resting Blood Pressure Data')
plt.ylabel('Number of Person')
plt.xlabel('Resting Blood Pressure')
plt.show()


true_rbp_data = data[data.target==1]['trestbps']
print("Diseased Resting Blood Pressure Data")
print("Minimum BP:"+str(min(true_rbp_data)))
print("Maximum BP:"+str(max(true_rbp_data)))
print("Average BP:"+str(np.mean(true_rbp_data)))
print("Median BP:"+str(np.median(true_rbp_data)))
plt.figure(5)
plt.hist(true_rbp_data, bins=8)
plt.title('Diseased Resting Blood Pressure Data')
plt.xlabel('Resting Blood Pressure')
plt.ylabel('Number of Person')
plt.show()


# Compare diseased and non-diseased people with ECDF
x1, y1 = ecdf(true_rbp_data)
false_rbp_data = data[data.target==0]['trestbps']
x2, y2 = ecdf(false_rbp_data)
plt.figure(6, figsize=(10,7))
plt.scatter(x1, y1, marker='.')
plt.scatter(x2, y2, marker='.')
plt.legend(['Diseased', 'Non-diseased'])
plt.title("Comparison between diseased and non-diseased people's RBP")
plt.xlabel('Resting Blood Pressure')
plt.ylabel('ECDF')
plt.show() 

#Cholesterol analysis
chol_data = data['chol']
print("Total Cholesterol Data")
print("Minimum Cholesterol:"+str(min(chol_data)))
print("Maximum Cholesterol:"+str(max(chol_data)))
print("Average Cholesterol:"+str(np.mean(chol_data)))
print("Median Cholesterol:"+str(np.median(chol_data)))
plt.figure(7)
plt.hist(rbp_data, bins=8)
plt.title('Total Cholesterol Data')
plt.ylabel('Number of Person')
plt.xlabel('Cholesterol')
plt.show()


true_chol_data = data[data.target==1]['chol']
print("Diseased Cholesterol Data")
print("Minimum Cholesterol:"+str(min(true_chol_data)))
print("Maximum Cholesterol:"+str(max(true_chol_data)))
print("Average Cholesterol:"+str(np.mean(true_chol_data)))
print("Median Cholesterol:"+str(np.median(true_chol_data)))
plt.figure(8)
plt.hist(true_rbp_data, bins=8)
plt.title('Diseased Cholesterol Data')
plt.xlabel('Cholesterol')
plt.ylabel('Number of Person')
plt.show()


false_chol_data = data[data.target==0]['chol']
chol_com_data = [true_chol_data, false_chol_data]
plt.figure(8)
plt.boxplot(chol_com_data)
plt.title("Comparing cholesterol for people with heart disease and healthy people")
plt.xticks([1,2], [True, False])
plt.ylabel("Cholesterol")
plt.show()