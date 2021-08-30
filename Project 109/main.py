import pandas as pd
import plotly.figure_factory as pff
import statistics 
import random

df = pd.read_csv('StudentsPerformance.csv')
mathsScore = df['math score'].tolist()

mean = statistics.mean(mathsScore)
mode = statistics.mode(mathsScore)
median = statistics.median(mathsScore)
std = statistics.stdev(mathsScore)
print("Mean :",mean)
print("Mode :",mode)
print("Median :",median)
print("Standard Deviation :",std)

#firstStandardDeviation
fendingP,fstartingP = mean - std,mean + std
firststd = []

for a in mathsScore :
    if(a>=fstartingP and a<=fendingP) :
        firststd.append(a)

firstpercent = len(firststd)/len(mathsScore) * 100
print(str(firstpercent)+"%", "of data lies within 2nd Standard Deviation")

#SecondStandardDeviation
sendingP,sstartingP = mean - (2*std),mean + (2*std)
secondstd = []

for a in mathsScore :
    if(a>=sstartingP and a<=sendingP) :
        secondstd.append(a)

secondpercent = len(secondstd)/len(mathsScore) * 100
print(str(secondpercent)+ "%","of data lies within 2nd Standard Deviation")

#ThirdStandardDeviation
tstartingP,tendingP = mean - (3*std),mean + (3*std)
thirdstd = []

for a in mathsScore :
    if(a>=tstartingP and a<=tendingP) :
        thirdstd.append(a)

thirdpercent = len(thirdstd)/len(mathsScore) * 100
print(str(thirdpercent)+ "%","of data lies within 3rd Standard Deviation")
