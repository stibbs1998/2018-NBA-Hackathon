import numpy as np
import csv
import matplotlib.pylab as plt

natl = np.loadtxt('../National_Ratings_by_Game.csv',delimiter=',',dtype=str)

for season in ['2014-15','2015-16','2016-17','2017-18']:

	home = natl[:,7]=='GSW'
	away = natl[:,8]=='GSW'
	dub_city = np.logical_or(home,away)	
	year = natl[:,0]==season
	network = natl[:,2]!='NBA TV'
	net_year = np.logical_and(network,year)
	kd_is_snake = np.logical_and(dub_city,net_year)
	ratings_per_year = (natl[kd_is_snake][:,9])
	ratings_per_year = ratings_per_year.astype(np.float)
	print('National Ratings for Golden State in %s were on average %.2f.' % (season, np.nanmean(ratings_per_year)))
