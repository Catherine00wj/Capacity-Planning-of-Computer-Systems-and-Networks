import numpy as np
# import seaborn as sns
import matplotlib.pyplot as pl
import math
from  scipy import stats
import simulation
import random
from  scipy import stats

total_list = []
tem_list =[]
index_list =[]
time = 15
pro = 0.95

for i in range(15):
    print("lopp---",i)
    ppp = []
    finish_job = simulation.simulation_method("random",[0.35],[1],5,5,9,5000)
    for n in range(len(finish_job)):
        if float(finish_job[n].split(" ")[2]) > 3000:
            ppp.append(float(finish_job[n].split(" ")[2]) -float(finish_job[n].split(" ")[1]))
    tem_list.append(np.mean(ppp))
tem_n =0
print("---------",len(tem_list))
for j in range(len(tem_list)):
    # tem_n = (tem_list[0][n].split(" ")[2] -tem_list[0][n].split(" ")[1]) + (tem_list[1][n].split(" ")[2] -tem_list[1][n].split(" ")[1]) +(tem_list[2][n].split(" ")[2] -tem_list[2][n].split(" ")[1])+(tem_list[3][n].split(" ")[2] -tem_list[3][n].split(" ")[1])+(tem_list[4][n].split(" ")[2] -tem_list[4][n].split(" ")[1])
    tem_n =  tem_n + tem_list[j]
mean = tem_n/15
#-----------divation-------
aa = np.std(tem_list,ddof =1)
bb = stats.t.ppf(1 - (1 - pro) / 2, 14)
temp = bb * aa / np.sqrt(15)
upper = mean +  temp
down = mean - temp
print(upper,down)
print("mean-----",mean)

# p = 0.95
# n = 15


# w = 10
# total_list = []
# for i in range (0,15):
#     with open("test_"+str(i+1)+".txt") as f:
#         store_list =[]
#         for line in f.readlines():
#             aa = line.split("\n")[0].split("        ")
#             print(aa)
#             bb = round((float(aa[1]) -float(aa[0])),3)
#             store_list.append(bb)
#     total_list.append(store_list)
#     print(store_list)
#     print(len(store_list))
# new_list =[]
#
# for j in range(0,1500):
#     mean_nb = 0
#     for k in range(len(total_list)):
#         mean_nb = mean_nb + total_list[k][j]
#     new_list.append(round(mean_nb/5,3))
# print(new_list)
# print(len(new_list))
#
# new_mean = [0] * (len(new_list)-w)
#
# for i in range(1,len(new_list)-w):
#     if (i <= w):
#         new_mean[i] = np.mean(new_list[0:(2*i-1)])
#     else:
#         new_mean[i] = np.mean(new_list[(i-w):(i+w)])
# print(new_mean)
#
# new_index =[]
# for i in  range(len(new_mean)):
#     new_index.append(i)
# pl.plot(new_index, new_mean)
# pl.xlabel('Index')
# pl.ylabel('Response-time')
# pl.title('Suitable value of Tc')
# pl.show()
# total =0
# count = 0
# for j in range(50,len(new_mean)):
#     total = total + new_mean[j]
#     count +=1
# print(total/count)
#-------------------------------------------------arrival——time-exponential-distribution--------------------------
# with open("arrival_time_1.txt") as f:
#     arrival_list = []
#     for line in f.readlines():
#         aa = line.split("\n")[0]
#         # print()
#         # bb = round((float(aa[1]) - float(aa[0])), 3)
#         arrival_list.append(float(aa))
# print(arrival_list)
# print(np.max(arrival_list))
# new =[]
# for i in range(0,len(arrival_list)-1):
#     new.append(arrival_list[i+1] -arrival_list[i])
# print(new)
# bins = []
# new_bins=[]
# tt= np.max(new)/50
# for i in range(0,50-1):
#     bins.append([i*tt,(i+1)*tt])
# print(bins)
# count = [0]*49
# for k in range(len(new)):
#     for m in range(len(bins)):
#         if bins[m][0] <= new[k] <= bins[m][1]:
#             count[m] +=1
# for j in range(len(bins)):
#     new_bins.append(j)
# print(new_bins)
# print(count)
# pl.plot(new_bins, count)
# pl.xlabel('Bins')
# pl.ylabel('Frequency')
# pl.title('Exponential Distribution')
# pl.show()

#-------------------------------------------------service-time-exponential-distribution---------------------------
# with open("service_time_1.txt") as f:
#     arrival_list = []
#     for line in f.readlines():
#         aa = line.split("\n")[0]
#         # print()
#         # bb = round((float(aa[1]) - float(aa[0])), 3)
#         arrival_list.append(float(aa))
# print(arrival_list)
# print(np.max(arrival_list))
# bins = []
# new_bins=[]
# tt= np.max(arrival_list)/50
# for i in range(0,50-1):
#     bins.append([i*tt,(i+1)*tt])
# print(bins)
# count = [0]*49
# for k in range(len(arrival_list)):
#     for m in range(len(bins)):
#         if bins[m][0] <= arrival_list[k] <= bins[m][1]:
#             count[m] +=1
# for j in range(len(bins)):
#     new_bins.append((bins[j][0] + bins[j][1]) / 2)
# print(new_bins)
# print(count)
# pl.plot(new_bins, count)
# pl.xlabel('Bins')
# pl.ylabel('Frequency')
# pl.title('Service_time Distribution')
# pl.show()
