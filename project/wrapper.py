import simulation
with open("num_tests.txt") as f:
    test_num = 0
    for line in f.readlines():
        test_num =line
for i in range(int(test_num)):
    final_job = []
    with open("arrival_"+str(i+1)+".txt") as f:
        arrival_time = []
        for line in f.readlines():
            arrival_time.append(round(float(line.split("\n")[0]) , 3))
        # print("arr " ,arrival_time)
    with open("para_"+str(i+1)+".txt") as f:
        ore_data = []
        for line in f.readlines():
            ore_data.append(line.split("\n")[0])
        # print("or-- " ,ore_data)
        SetupTime = float(ore_data[1])
        DelayoffTime = float(ore_data[2])
        ServerNum = int(ore_data[0])
    with open("service_"+ str(i+1) + ".txt") as f:
        service_time = []
        for line in f.readlines():
            service_time.append(round(float(line.split("\n")[0]) , 3))
        # print("ser---" ,service_time)
    with open("mode_"+ str(i+1) + ".txt") as f:
        mode =""
        for line in f.readlines():
            mode = line.strip()
        # print("mo----",mode)
    if mode == "trace":
        final_job = simulation.simulation_method(mode,arrival_time,service_time,ServerNum,SetupTime,DelayoffTime,time_end =0)
    if mode =="random":
        TimeEnd = float(ore_data[3])
        # for j in range(15):
        final_job = simulation.simulation_method(mode, arrival_time, service_time, ServerNum, SetupTime, DelayoffTime,TimeEnd)
        # total_time = 0.0
        # total_num = len(final_job)
        # # with open('./test_5.txt', 'w') as f:
        #     for k in range(len(final_job)):
        #         f.write(final_job[k].split(" ")[1] + "        " + final_job[k].split(" ")[2] + "\n")
        #         total_time = total_time + (float(final_job[k].split(" ")[2]) - float(final_job[k].split(" ")[1]))
        # with open('./mrt_1.txt', 'w') as f:
            # print(i)
            # f.write(str(round(total_time / total_num, 3)))
    total_time = 0.0
    total_num  =len(final_job)
    with open('./departure_' + str(i+1) + '.txt', 'w') as f:
        for j in range(len(final_job)):
            aa = float(final_job[j].split(" ")[1])
            bb =float(final_job[j].split(" ")[2])
            print(aa)
            print(bb)
            f.write('%.3f'%aa+ "\t" + '%.03f'%bb +"\n")
            total_time = total_time + (float(final_job[j].split(" ")[2]) -float(final_job[j].split(" ")[1]))
    with open('./mrt_' + str(i+1) + '.txt', 'w') as f:
        print(i)
        f.write(str('%.3f'%(round(total_time/total_num,3))))

