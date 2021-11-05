# Author: Payam Ghassemi, payamgha@buffalo.edu
# Sep 8, 2018
# Copyright 2018 Payam Ghassemi

import numpy as np

from matplotlib import pyplot as plt

import scipy.io

import pickle

# Built-in python libraries
import sys
import os
from urllib.request import urlretrieve

# 3rd-party libraries I'll be using
import matplotlib
from matplotlib import pyplot as plt

import pandas as pd
import seaborn as sns

from scipy import stats

matplotlib.rcParams['text.usetex'] = False
matplotlib.rcParams['lines.markeredgewidth'] = 1

def set_style(font_size=12, is_seabron=True):
    if is_seabron:
        plt.style.use(['seaborn-white', 'seaborn-paper'])
    else:
        plt.style.use(['classic'])    
    font = {'family' : 'serif',
            'weight' : 'normal',
            'size'   : font_size}
    ticks = {}
    # font = {'family':'Times New Roman',
    #         'weight' : 'normal',
    #         'size'   : 12}
    plt.tick_params(which="major", direction="in")
    matplotlib.rc("font", **font)


def set_size(fig, width=6, height=3):
    fig.set_size_inches(width, height)
    plt.tight_layout()

def get_colors():
    return np.array([
        [0.1, 0.1, 0.1],          # black
        [0.4, 0.4, 0.4],          # very dark gray
        [0.7, 0.7, 0.7],          # dark gray
        [0.9, 0.9, 0.9],          # light gray
        [0.984375, 0.7265625, 0], # dark yellow
        [1, 1, 0.9]               # light yellow
    ])

def set_color_palette():
    flatui = [ "#2ecc71", "#C3CED0", "#1DABE6", "#1C366A",  "#106f96", "#E43034", "#3498db", "#e74c3c","#a65d42","#6e5200","#dcc4d2"]
    palette_B = sns.set_palette(flatui)
