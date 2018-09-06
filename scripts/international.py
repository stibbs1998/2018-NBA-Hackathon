import numpy as np
import matplotlib.pylab as plt

intl = np.loadtxt('../Updated_International_League_Pass_Viewership.csv',dtype=str,delimiter=',')
# season # home # away # date # EST military # country # num_viewers # min_view
print(intl)
