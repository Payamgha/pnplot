# Author: Payam Ghassemi, payamgha@buffalo.edu
# Copyright 2020 Payam Ghassemi

import numpy as np
import pandas as pd
import seaborn as sns

from scipy.stats import zscore

from matplotlib import pyplot as plt

from scipy.spatial import distance as dist

import scipy.io

import pickle

import networkx as nx

from time import time, sleep

from pnplot import *

n_scenario = 100

# Read the results
#results_bigmrta = pickle.load(open("results-bigmrta"+".pkl","rb"))
header_sns = ["Method", "Epoch", "Cost"]
header = ["CAM", "AM"]
n_robot = 20
results = pickle.load(open("convergence.pkl","rb"))
n_epochs = 200
performance = np.zeros((n_epochs*2, 3))
i_instance = 0
for i_epoch in range(n_epochs):
    performance[i_instance, :] = [0, i_epoch, results["CAM"][i_epoch]]
    print(performance[i_instance, :])
    i_instance += 1
    performance[i_instance, :] = [1, i_epoch, results["AM"][i_epoch]]
    print(performance[i_instance, :])
    i_instance += 1
    
df_performance = pd.DataFrame(performance, columns=header_sns)


fig = plt.figure() # Create matplotlib figure
ax = fig.add_subplot(111) # Create matplotlib axes
#df_obj_cost_scenarios.boxplot()
sns.lineplot(x='Epoch', y='Cost', hue='Method', style='Method', markers=False, dashes=False, data=df_performance) 
#plt.xticks(ticks=[0,1], labels=header)
plt.xlabel("Epoch")
plt.ylabel("Cost Function")
#plt.ylim([0.,0.2])
plt.legend(("CAM", "AM"), loc="lower right")
#plt.hlines(y=0,xmin=50,xmax=200, linestyles="dashed",colors="#C3CED0")
set_size(plt.gcf(), width=3, height=2)
plt.savefig("convergence_performance_cost.pdf", format="pdf", dpi=300, bbox_inches='tight')
plt.show()
