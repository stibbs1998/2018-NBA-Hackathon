import numpy as np
import csv
import matplotlib.pylab as plt

natl = np.loadtxt('../National_Ratings_by_Game.csv',delimiter=',',dtype=str)
teams,tvs = np.loadtxt('../DMA_Households.csv',delimiter=',',skiprows=1,dtype=str,unpack=True)
tvs = tvs.astype(np.float)

print(tvs)

for season in ['2014-15','2015-16','2016-17','2017-18']:

	r = []
	xticks = []	

	for team in np.unique(natl[1:,8]):
		home = natl[:,7]== team
		away = natl[:,8]== team
		dub_city = np.logical_or(home,away)	
		year = natl[:,0]==season
		# decided to exclude NBA TV as this is a premium national 
		# viewership audience
		network = natl[:,2]!='NBA TV'
		net_year = np.logical_and(network,year)
		kd_is_snake = np.logical_and(dub_city,net_year)
		ratings_per_year = (natl[kd_is_snake][:,9])
		ratings_per_year = ratings_per_year.astype(np.float)
		xticks.append(team)
		if len(ratings_per_year)!=0:
			r.append(np.nanmean(ratings_per_year)) # avg nat'l rating	
		else:
			r.append(np.nan)
	
	plt.figure(figsize=(12,6))
	x = np.linspace(0,29,30)
	plt.scatter(x,r)
	plt.xticks(x,xticks,rotation=70)
	plt.ylabel("Nat'l TV Rating")
	plt.title("Average nat'l rating for teams in %s" %season)
	plt.ylim(0,3)
	plt.show()
