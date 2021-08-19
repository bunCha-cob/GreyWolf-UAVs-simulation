import matplotlib.pyplot as plt
import numpy as np

output1 = []
output2 = []

f = open("test1.txt", "r")
win_count1 = 0
win_count2 = 0

for x in f:
    x_split = x.split();
    if (x_split[0] == "w"):
        win_count1 += 1;
        run_time = float(x_split[1])
        output1.append(run_time)
f.close()

f = open("output2.txt", "r")
for x in f:
    x_split = x.split();
    if (x_split[0] == "w"):
        win_count2 += 1;
        run_time = float(x_split[1])
        output2.append(run_time)
f.close()

times1 = np.arange(1,len(output1)+1)
times2 = np.arange(1,len(output2)+1)
fig, axs = plt.subplots(1, 2)
fig.suptitle('Run time comparison')
axs[0].plot(times1, output1)
axs[1].plot(times2, output2)

axs[0].set_title('average run-time(without GWB) = ' + "{:.2f}".format(sum(output1)/len(output1)) + "s")
axs[1].set_title('average run-time(with GWB) = ' + "{:.2f}".format(sum(output2)/len(output2)) + "s")
axs[0].set(xlabel='Number of battles won: ' + str(win_count1) + " (win rate : " + "{:.2f}".format(win_count1/10) + "%)", ylabel='run time (seconds)')
axs[1].set(xlabel='Number of battles won: ' + str(win_count2) + " (win rate : " + "{:.2f}".format(win_count2/10) + "%)")
plt.show()