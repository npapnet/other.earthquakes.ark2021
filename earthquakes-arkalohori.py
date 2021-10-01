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
# %%
df['post'] = df.index < max_loc
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
df['date'] = df.timestamp.apply(lambda x: x.date())
sns.scatterplot(x='timestamp', y='mag', data = df.iloc[:max_loc+1,:], ax =axs)
sns.lineplot(x='date', y='mag', data = df.iloc[:max_loc+1,:], ax =axs)
# %%
plt.show()