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
output_name = "./PR10_FCN_layer.txt"
f = open(output_name, 'w')

interest_word1 = "hpp:77]"
interest_word2 = "Top shape: "
with open("PR10_FCN_trainingLog.txt", "r") as file:
#with open("./pretrain.txt", "r") as ins:
    for line in file:
        if interest_word1 in line:
            layer_name = line[line.index(interest_word1) + len(interest_word1):]
            f.write ("                     "+"\n")
            f.write(layer_name+"\n")
        if interest_word2 in line:
            layer_dim = line[line.index(interest_word2) + len(interest_word2): line.index("(")]
            f.write(layer_dim+"\n")
