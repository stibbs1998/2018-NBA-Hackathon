import numpy as np
import matplotlib.pylab as plt

data = np.loadtxt('RSN_Ratings_by_Game.csv',delimiter = ',', dtype = str)
teams, tvs  = np.loadtxt('DMA_Households.csv',delimiter = ',', dtype = str, unpack = True, skiprows = 1)

teams = np.delete(teams,27)
tvs = np.delete(tvs,27)

tvs = tvs.astype(np.float)

r_home = []
r_away = []
for team in np.unique(data[1:,7]):
        if team != 'TOR':
                team_r_home = data[data[:,7] == team]
                tr_away = data[data[:,6] == team]
                home_network = team_r_home[:,16]
                home_network[home_network==''] = np.nan
                home_network[home_network=='<<'] = np.nan

                home_network = home_network.astype(np.float)
                away_network = tr_away[:,10]
                away_network[away_network==''] = np.nan
                away_network[away_network=='<<'] = np.nan
                away_network = away_network.astype(np.float)

                avg = np.nanmean(home_network)
                avgaway = np.nanmean(away_network)
                r_home.append(avg)
                r_away.append(avgaway)
colors = np.arange(29)
xticks = np.arange(29)
print(len(xticks),len(r_home))
plt.figure()
plt.scatter(xticks,r_home,s=5*np.pi*tvs**2,c=colors)
plt.xticks(np.arange(29),list(teams),rotation=75)
plt.ylabel('Local TV Rating')
plt.title('TV Rating vs. Size of Market')
plt.savefig('ratingVsize.png')
plt.show()

