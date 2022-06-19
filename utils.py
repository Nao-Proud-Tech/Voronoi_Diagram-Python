# ====================
# Library to Import
# ====================
import random
import numpy as np
import matplotlib.pyplot as plt

# Random Without Duplication
def rand_ints_nodup():
    rand_table = list(range(256))
    shuffle_table = random.shuffle(rand_table)
    return shuffle_table


# Get Color Map
def get_cmap_ours(name):

    cm = plt.get_cmap(name)

    Rs = []
    Gs = []
    Bs = []
    As = []

    for n in range(256):
        Rs.append(cm(n)[0])
        Gs.append(cm(n)[1])
        Bs.append(cm(n)[2])
        As.append(cm(n)[3])

    return Rs, Gs, Bs, As