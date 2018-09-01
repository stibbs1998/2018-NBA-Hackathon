import numpy as np
import csv
import matplotlib.pylab as plt

local = np.loadtxt('RSN_Ratings_by_Game.csv', delimiter = ',', dtype = str)
# home = local[:,7], home rating = local[:,16], home channel = local[:,14]
# away = local[:,6], away rating = local[:,10], away channel = local[:,8]
teams = []
ratings = []
r_away = []
for team in np.unique(local[1:,7]):
	if team != 'TOR':
		team_ratings = local[local[:,7] == team]
		tr_away = local[local[:,6] == team]
		home_network = team_ratings[:,16]
		home_network[home_network==''] = np.nan
		home_network[home_network=='<<'] = np.nan

		home_network = home_network.astype(np.float)
		away_network = tr_away[:,10]
		away_network[away_network==''] = np.nan
		away_network[away_network=='<<'] = np.nan
		away_network = away_network.astype(np.float)

		avg = np.nanmean(home_network)
		avgaway = np.nanmean(away_network)
		teams.append(team)
		ratings.append(avg)
		r_away.append(avgaway)

def sort_list(l1, l2):
	zipped_pairs = zip(l1,l2)
	z = [x for _, x in sorted(zipped_pairs)]
	return z

t_sort = (sort_list(ratings,teams))
ratings.sort()
for i in range(len(t_sort)):
	print(ratings[i], t_sort[i])	

t_sortaway = sort_list(r_away,teams)

r_away.sort()
for i in range(len(t_sortaway)):
	print(r_away[i],t_sortaway[i])

all_homeratings = local[1:,16]
all_homeratings[all_homeratings=='']=np.nan
all_homeratings[all_homeratings=='<<']=np.nan
all_homeratings = all_homeratings.astype(np.float)

all_awayratings = local[1:,10]
all_awayratings[all_awayratings=='']=np.nan
all_awayratings[all_awayratings=='<<']=np.nan
all_awayratings = all_awayratings.astype(np.float)


plt.figure()
plt.plot(all_homeratings,'b.',markersize = 0.7,label='home_TV')
plt.plot(all_awayratings,'r.',markersize = 0.7,label='away_TV')
plt.tick_params(
axis='x',
which='both',
bottom = False,
top= False,
labelbottom=False)

plt.title("All TV Ratings for U.S. Local Markets")
plt.legend()
plt.savefig("all_games.png")
plt.show()

plt.figure()
plt.plot(ratings,'bo',label="Home")
plt.tick_params(
axis='x',
which='both',
bottom = False,
top= False,
labelbottom=False)

plt.plot(r_away,'ro',label="Away")
plt.legend()
plt.title("Average U.S. Local Market TV Ratings (both ordered low to high)")
plt.savefig("avg_ratings.png")
plt.show()
