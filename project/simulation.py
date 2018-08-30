import random
import math
#-------------------------------------- start system-----------------------------------------------
def simulation_method(mode,arrival,service,m,setup_time,delayoff_time,time_end =0):
    time =0.0
    current_time = 0.0
    waiting_list = []
    job_list = []
    finished_job = []
    arrival_time =[]
    service_time = []
    total_record = []
    off = []
    for i in range(m):
        off.append(str(i + 1))
    total_record.append(off)
    setup = []
    total_record.append(setup)
    busy = []
    total_record.append(busy)
    delayoff = []
    total_record.append(delayoff)
    # delayoff =[]
    # delayoff.append(str(1) + "," + str(10))
    # delayoff.append(str(2) + "," + str(10))
    # total_record = [[str(3)],[],[],delayoff]
    # print(total_record)
    ServerNum = m
    SetupTime = setup_time
    DelayoffTime = delayoff_time
    if mode == "trace":
        arrival_time = arrival
        service_time = service
        for j in range(len(service_time)):
            job_list.append(str(j + 1) + " " + str(arrival_time[j]) + " " + str(service_time[j]) + " " + "num" + " " + "unmarked")
    # random.seed(1)
    def random_number(number):
        aa = random.uniform(0,1)
        return - math.log(1-aa)/number
        # return random.expovariate(number)
    if mode == "random":
        current_time = random_number(arrival[0])
        while current_time <= float(time_end):
            arrival_time.append(round(current_time,3))
            ser_time = round((random_number(service[0]) + random_number(service[0]) +random_number(service[0])),3)
            service_time.append(ser_time)
            tem_t = random_number(arrival[0])
            current_time = current_time + tem_t
        # print(len(service_time))
        recor =[]
        for i in range (0,len(arrival_time)-1):
            if arrival_time[i] == arrival_time[i+1]:
                recor.append(i)
        new_arr = []
        new_ser =[]
        for j in range(len(arrival_time)):
            count =0
            for k in (recor):
                if j!=k:
                    count +=1
            if count == len(recor):
                new_arr.append(arrival_time[j])
                new_ser.append(service_time[j])
        arrival_time =new_arr
        service_time = new_ser
        # with open('arrival_time_5.txt', 'w') as f:
        #     for m in range(len(arrival_time)):
        #         f.write(str(arrival_time[m]) + "\n")
        # with open('service_time_5.txt', 'w') as f:
        #     for n in range(len(service_time)):
        #         f.write(str(service_time[n]) + "\n")
        for j in range(len(service_time)):
            job_list.append(str(j + 1) + " " + str(arrival_time[j]) + " " + str(service_time[j]) + " " + "num" + " " + "unmarked")
    while len(finished_job) != len(service_time) or len(total_record[0]) != ServerNum :
        if len(job_list) >0 and round(float(job_list[0].split(" ")[1]),3) == round(time,3):
            waiting_list.append(job_list[0])
            job_list = job_list[1:len(job_list)]
            print("----waiting--------- ",waiting_list)
            # print(total_record)
            if len(total_record[3]) < len(waiting_list):
                if len(total_record[3]) >0 :
                    tem_list = []
                    tem_list = waiting_list[0].split(" ")
                    tem_sta  = total_record[3][0]
                    tem_time = round(float(tem_list[2]),3) + round(float(tem_sta.split(",")[1]),3)
                    total_record[2].append(tem_sta.split(",")[0] + "," +str(round(tem_time,3)))
                    finished_job.append(str(tem_list[0]) + " " + waiting_list[0].split(" ")[1] +" "+ str(round(tem_time,3)))
                    waiting_list = waiting_list[1:len(waiting_list)]
                    total_record[3] = total_record[3][1:]
            if len(total_record[3]) >= len(waiting_list):
                if len(waiting_list)>0 and len(total_record[3]) != 0:
                    tem = total_record[3][0]
                    tem_time = round(time ,3)  + round(float(waiting_list[0].split(" ")[2]),3)
                    total_record[2].append(tem.split(",")[0] + "," + str(round(tem_time,3)))
                    finished_job.append(waiting_list[0].split(" ")[0] + " " + waiting_list[0].split(" ")[1] +" " + str(round(tem_time,3)))
                    waiting_list = waiting_list[1:len(waiting_list)]
                    total_record[3] = total_record[3][1:]
            if len(total_record[0]) != 0  and len(total_record[3]) ==0:
                if len(total_record[0]) < len(waiting_list):
                    if  len(total_record[0]) >0:
                        for i in range(len(waiting_list)):
                            tem_list = waiting_list[i].split(" ")
                            if tem_list[3 ] == "num":
                                tem_sta = total_record[0].pop()
                                tem_time = round(float(tem_list[1]),3) + SetupTime
                                total_record[1].append(tem_sta + "," + str(round(tem_time,3)))
                                waiting_list[i] = tem_list[0] + " " + tem_list[1] + " " + tem_list[2] + " " + tem_sta.split(",")[0]  + " " + "SetUp"
                if len(total_record[0]) >= len(waiting_list):
                        for i in range(len(waiting_list)):
                            tem_list = waiting_list[i].split(" ")
                            if tem_list[3] == "num":
                                tem_sta = total_record[0].pop()
                                tem_time = round(float(tem_list[1]),3) + SetupTime
                                total_record[1].append(tem_sta + "," + str(round(tem_time,3)))
                                waiting_list[i] = tem_list[0] + " " + tem_list[1] + " " + tem_list[2] + " " + tem_sta.split(",")[0] + " " + "SetUp"
    #-----------------------------from SETUP to BUSY------------------------------------------------------------
        if len(total_record[1]) !=0 and len(waiting_list) != 0:
            if round(float(total_record[1][0].split(",")[1]) ,3)== round(time,3):
                tem_list = []
                tem_list = waiting_list[0].split(" ")
                tem_sta = total_record[1][0]
                tem_time =  round(time,3) + round(float(tem_list[2]),3)
                total_record[2].append(tem_sta.split(",")[0] + "," + str(round(tem_time,3)) )
                finished_job.append(waiting_list[0].split(" ")[0] + " " + waiting_list[0].split(" ")[1] + " " + str(round(tem_time,3)))
                waiting_list = waiting_list[1:len(waiting_list)]
                total_record[1] = total_record[1][1:]
    #-------------------------------from BUSY to DELAYOFF------------------------------------------------------
        if len(total_record[2]) != 0:
            # print("---busy-----", total_record)
            new_busy = []
            for i in range(len(total_record[2])):
                if round(float(total_record[2][i].split(",")[1]),3)== round(time,3):
                    if len(waiting_list) != 0:
                        tem_list = waiting_list[0].split(" ")
                        tem_time = round(float(waiting_list[0].split(" ")[2]),3) + round(time ,3)
                        finished_job.append(waiting_list[0].split(" ")[0] + " " + waiting_list[0].split(" ")[1] + " " + str(round(tem_time,3)))
                        if tem_list[4] == "SetUp" :
                            count =0
                            for m in range(len(waiting_list)):
                                if waiting_list[m].split(" ")[4] == "unmarked":
                                    waiting_list[m] = waiting_list[m].split(" ")[0] +" " + waiting_list[m].split(" ")[1] +" " + waiting_list[m].split(" ")[2] + " " + tem_list[3] +" " + "SetUp"
                                    count +=1
                                    break
                            if count  == 0 :
                                aa = total_record[1].pop()
                                total_record[0].append(aa.split(",")[0])
                                # print("busy-time------------ ", total_record)
                        waiting_list = waiting_list[1:len(waiting_list)]
                        total_record[2][i] = total_record[2][i].split(",")[0] + ","+ str(round(tem_time,3))
                        new_busy.append(total_record[2][i])
                    else:
                        total_record[3].append(total_record[2][i])
                else:
                    new_busy.append(total_record[2][i])
            total_record[2] = new_busy

    #--------------------------------from DELAYOFF to BUSY-----------------------------------------------------
        if len(total_record[3]) != 0:
            new_delayoff = []
            for i in range(len(total_record[3])):
                if round((float(total_record[3][i].split(",")[1]) + DelayoffTime ),3)== round(time ,3) :
                    # print("jieshu----",round(time ,3)," ", total_record[3][i])
                    total_record[0].append(total_record[3][i].split(",")[0])
                if round(float(total_record[3][i].split(",")[1]),3) <= round(time,3) < round((float(total_record[3][i].split(",")[1] )+ DelayoffTime),3):
                    # print("stillbusuy------",round(time ,3)," " , total_record[3][i]," ", round((float(total_record[3][i].split(",")[1] )+ DelayoffTime),3))
                    if len(waiting_list) != 0 :
                        # print("----delauy",total_record)
                        # print("witing---now----",waiting_list)
                        tem = total_record[3][i]
                        tem_time = round(time,3) + round(float(waiting_list[0].split(" ")[2]),3)
                        finished_job.append(waiting_list[0].split(" ")[0] + " " + waiting_list[0].split(" ")[1] + str(round(tem_time,3)))
                        waiting_list = waiting_list[1:len(waiting_list)]
                        total_record[2].append(tem.split(",")[0] + "," + str(round(tem_time,3)))
                    else:
                        new_delayoff.append(total_record[3][i])
                        # print("toto---", new_delayoff)
            total_record[3] = new_delayoff
            # print("---delayoff-----", total_record)
        time = round((time + 0.001) ,3)
    if mode == "random":
        # print(len(finished_job))
        final =[]
        for i in range(len(finished_job)):
            if round(float(finished_job[i].split(" ")[2]),3)<= round(float(time_end),3):
                final.append(finished_job[i])
        finished_job = final
    tem_store=[]
    new_sore = []
    nb_list =[]
    for m in range(len(finished_job)):
        tem_store.append(float(finished_job[m].split(" ")[2]))
    tem_store.sort()
    for n in range(len(tem_store)):
        for k in range(len(finished_job)):
            if tem_store[n] == float(finished_job[k].split(" ")[2]) and k not in nb_list:
                new_sore.append(finished_job[k])
                nb_list.append(k)
    finished_job = new_sore
    return finished_job





# arrival_time =[10,18,20,23,28,32,33,34,35,57,86,92]
# service_time =[2,4,14,5,6,21,2,16,9,4,15,9]
# final_job = simulation_method("trace", arrival_time, service_time, 3, 50, 100,1)
# print(final_job)
# total_time = 0.0
# total_num  =len(final_job)
# with open('test.txt', 'w') as f:
#     for j in range(len(final_job)):
#         aa = float(final_job[j].split(" ")[1])
#         bb = float(final_job[j].split(" ")[2])
#         print(aa)
#         print(bb)
#         f.write('%.3f' % aa + "\t" + '%.03f' % bb + "\n")
#         total_time = total_time + (float(final_job[j].split(" ")[2]) - float(final_job[j].split(" ")[1]))
# print("mean response time : " ,str('%.3f'%(round(total_time/total_num,3))))






# arrival_time =[11,11.2,11.3,13]
# service_time =[1,1.4,5,1]
# final_job = simulation_method("trace", arrival_time, service_time, 3, 5, 10,1)
# print(final_job)
# total_time = 0.0
# total_num  =len(final_job)
# with open('test.txt', 'w') as f:
#     for j in range(len(final_job)):
#         aa = float(final_job[j].split(" ")[1])
#         bb = float(final_job[j].split(" ")[2])
#         print(aa)
#         print(bb)
#         f.write('%.3f' % aa + "\t" + '%.03f' % bb + "\n")
#         total_time = total_time + (float(final_job[j].split(" ")[2]) - float(final_job[j].split(" ")[1]))
# print("mean response time : " ,str('%.3f'%(round(total_time/total_num,3))))












