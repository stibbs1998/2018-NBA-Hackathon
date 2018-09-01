import numpy as np
import csv
import matplotlib.pylab as plt

natl = np.loadtxt('National_Ratings_by_Game.csv',delimiter=',',dtype=str)
nnn = (natl[1:,9].astype(np.float))
nnn.sort()
print(nnn)

