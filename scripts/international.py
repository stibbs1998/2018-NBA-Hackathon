import numpy as np
import matplotlib.pylab as plt

intl = np.loadtxt('../International_League_Pass_Viewership.csv',dtype=str,delimiter=',')
# season # home # away # date # EST military # country # num_viewers # min_view
print(len(np.unique(intl[1:,3])),np.unique(intl[1:,3]))
