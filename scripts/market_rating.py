import numpy as np
import matplotlib.pylab as plt


def sort_list(l1, l2):
        zipped_pairs = zip(l1,l2)
        z = [x for _, x in sorted(zipped_pairs)]
        return z


data = np.loadtxt('../RSN_Ratings_by_Game.csv',delimiter = ',', dtype = str)
teams, tvs  = np.loadtxt('../DMA_Households.csv',delimiter = ',', dtype = str, unpack = True, skiprows = 1)

teams = np.delete(teams,27)
tvs = np.delete(tvs,27)

tvs = tvs.astype(np.float)

past = None

for season in ['2014-15','2015-16','2016-17','2017-18']:
	
	ratings = []

	for team in np.unique(data[1:,7]):
		if team != 'TOR':
			c_season = data[data[:,0]==season]
			team_r_home = c_season[c_season[:,7] == team]
			tr_away = c_season[c_season[:,6] == team]
			home_network = team_r_home[:,16]
			home_network[home_network==''] = np.nan
			home_network[home_network=='<<'] = np.nan
			home_network = home_network.astype(np.float)

			away_network = tr_away[:,10]
			away_network[away_network==''] = np.nan
			away_network[away_network=='<<'] = np.nan
			away_network = away_network.astype(np.float)


			all_games = list(away_network)+list(home_network)
			avg = np.nanmean(all_games)
			ratings.append(avg)
	
	team_ticks = sort_list(ratings,list(teams))
	sorted_tvs = sort_list(ratings,tvs)
	ratings.sort()
	avg_view = np.array(sorted_tvs)*10**4 * np.array(ratings) 
	colors = 14*np.ones(29)
	xticks = np.arange(29)
	plt.figure(figsize = (12,6))
	plt.scatter(xticks,ratings,s=5*np.pi*np.array(sorted_tvs)**2,c=colors)
	if type(past) != type(None):
		plt.scatter(xticks,past,c='r',s=5,label = 'Previous Season')
	plt.xticks(np.arange(29),team_ticks,rotation=75)
	plt.ylabel('Local TV Rating')
	plt.title('TV Rating vs. Size of Market in %s'%season)
	plt.legend()
#	plt.savefig('../plots/avg_rating%s.png'%season)
	plt.show()
	

	past = list(np.copy(ratings))

'''
	plt.figure(figsize = (12,6))
	plt.scatter(xticks,avg_view,s=5*np.pi*np.array(sorted_tvs)**2,c=colors)
	plt.xticks(np.arange(29),team_ticks,rotation = 75)
	plt.ylabel('Avg Viewers Per Game')
	plt.title('Avg Local Viewers Per Game in %s' %season)
	plt.ylim(0, 2.5*10**5)
#	plt.savefig('../plots/avg_views%s.png'%season)
	plt.show()


	past = list(np.copy(ratings))


'''
