#tr = "this is string example....wow!!!:wq!"
#print str.lstrip()
#str = "88888888this is string example....wow!!!8888888"
#print str.lstrip('8')
import os
import csv
import numpy as np

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

import matplotlib.pyplot as plt


loss = []


interest_word = ", loss = "

with open("./fcn_log_all.txt", "r") as file:
#with open("./pretrain.txt", "r") as ins:
    for line in file:
        if interest_word in line:
            loss_string = line[line.index(interest_word) + len(interest_word):]
            loss_number = float(loss_string)
            print loss_number
            loss.append(loss_number)
n = len(loss)
print n 
num_iter = n

x = np.arange(n)

majorLocator = MultipleLocator(num_iter)

fig, ax = plt.subplots()

plt.plot(x,loss,'-b',label='train loss')

#ax.xaxis.set_major_locator(majorLocator)
#ax.set_xticks(range(0,num_iter*30+1,num_iter))
#ax.set_xticklabels([j for j,i in enumerate(x)])
#ax.set_xlim([0,num_iter*30])
#plt.title('Loss curve for training from scratch')
plt.xlabel('x100 iterations')
plt.ylabel('Loss')

#plt.show()
plt.savefig('fcn_loss.jpg')




