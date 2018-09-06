import numpy as np
import matplotlib.pylab as plt
from operator import itemgetter

natl = np.loadtxt('../National_Ratings_by_Game.csv',dtype=str,delimiter=',')
teams,tvs = np.loadtxt('../DMA_Households.csv',dtype=str,delimiter=',',skiprows=1,unpack=True)

team = 'GSW' 
gs = team
home = natl[:,7]==gs
away = natl[:,8]==gs
played = np.logical_or(away,home)
all_dates = natl[:,3] # haystack
dates = natl[played][:,3] # needles
st = set(dates)
date_indicies = ([i for i, e in enumerate(all_dates) if e in st])
other_days = ([i for i, e in enumerate(all_dates) if e not in st])

# list of dates

day_gsw_televised = natl[date_indicies]
day_not_televised = natl[other_days]

print("National Ratings season to season: \n \n ")

for season in ['2014-15','2015-16','2016-17','2017-18']:

	all_year = natl[:,0]==season
	all_NoNBA = natl[:,2]!='NBA TV'
	ind1 = np.logical_and(all_NoNBA,all_year)
	all_r = natl[ind1][:,9]
	all_r = all_r.astype(np.float)
	

	year = day_gsw_televised[:,0]==season
	noNBATV = day_gsw_televised[:,2]!='NBA TV'
	ind = np.logical_and(year,noNBATV)
	no_GSWh = day_gsw_televised[:,7]!=team
	no_GSWa = day_gsw_televised[:,8]!=team
	no_GSW = np.logical_and(no_GSWh,no_GSWa)
	ind2 = np.logical_and(no_GSW,ind)
	
	ratings = day_gsw_televised[ind][:,9]
	ratings = ratings.astype(np.float)
	ratings_noGSW = day_gsw_televised[ind2][:,9]
	ratings_noGSW = ratings_noGSW.astype(np.float)	

	year = day_not_televised[:,0]==season
	noNBA = day_not_televised[:,2]!='NBA TV'
	ind = np.logical_and(noNBA,year)
	r2 = day_not_televised[ind][:,9]
	r2 = r2.astype(np.float)	

	print(season,'days GSW played INCLUDING GSW',np.nanmean(ratings))
	print(season,'days GSW played NOT INCLUDING GSW', np.nanmean(ratings_noGSW))
	print(season,'all games',np.nanmean(all_r))
	print(season,"days GSW doesn't play",np.nanmean(r2))
	print('\n\n')
	print('\n\n')


