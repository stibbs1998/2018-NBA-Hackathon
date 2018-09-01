import numpy as np

local = np.loadtxt('RSN_Ratings_by_Game.csv',delimiter=',', dtype=str)
atl = (local[local[:,0]=='2014-15'])
atl2 = atl[atl[:,7]=='ATL']

atl2[atl2=='']=np.nan
atl2[atl2=='<<']=np.nan
atl2 = (atl2[:,16])
atl2 = atl2.astype(np.float)
print(np.nanmean(atl2))
