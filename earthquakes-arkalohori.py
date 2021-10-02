#%% 

from matplotlib import markers
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
#%%

df = pd.read_csv('catalogue.csv', usecols=[0,1,2,3,4])
# rename columns
df.columns = ['timestamp', 'lat', 'long', 'depth', 'mag']
# convert 
df.timestamp = pd.to_datetime(df.timestamp.apply(lambda x : x[1:]))

# %% plot mag
df.mag.plot.hist()

# %%
max_loc = df.mag.idxmax()
# %%  # additional columns
df['post'] = df.index < max_loc
df['date'] = df.timestamp.apply(lambda x: x.date())

dts = [(df.timestamp[i]-df.timestamp[i+1]).total_seconds() for i in range(df.shape[0]-1)]
dts.append(0)
df['sec_before'] = dts
#%%
fig, axs = plt.subplots(nrows=1, ncols=2, sharey=True)

df.mag[max_loc:].plot.hist(ax=axs[0])
axs[0].grid()
axs[0].set_title('distribution pre max')
df.mag[:max_loc].plot.hist(ax=axs[1])
axs[1].grid()
axs[1].set_title('distribution after max')

# %%
fig, axs = plt.subplots(nrows=1, ncols=1,figsize=(20,15))
df.plot(x='timestamp', y='mag', lw=0, marker='.', ax=axs)
# %%
df.iloc[:max_loc+1,:].plot(x='timestamp', y='mag', lw=0, marker='.')
# %%
fig, axs = plt.subplots(nrows=1, ncols=1,figsize=(20,15))
sns.scatterplot(x='timestamp', y='mag', data = df.iloc[:max_loc+1,:], ax =axs)
sns.lineplot(x='date', y='mag', data = df.iloc[:max_loc+1,:], ax =axs)
# %%
plt.show()

# %%

    
# %%
df.iloc[:max_loc+1,:].sec_before.plot.kde(xlim = [0,1e4])
# %%
df.iloc[:max_loc+1,:].sec_before.plot.hist(xlim = [0,1e4])

#%%
df.iloc[:max_loc+1,:].plot.scatter(x='sec_before', y='mag', xlim= (0,10000))


# %%
fig, axs = plt.subplots(nrows=1, ncols=1,figsize=(20,15))
df.iloc[:max_loc+1,:].plot.scatter(x ='sec_before', y='mag', ax =axs, logx=True,xlim=[1,1e6])
# %%
