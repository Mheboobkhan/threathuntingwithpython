import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import sklearn

df = pd.read_csv('/home/wh/Desktop/bro/ml-analysis/conn.log.csv')
df = df.drop(columns = ['local_orig','local_resp','missed_bytes','tunnel_parents','history','conn_state'])

df.replace ('-', np.nan , inplace = True)

missing_data = df.isnull()
for column in missing_data.columns.values.tolist():
    print (column)
    print (missing_data[column].value_counts())
    print ("")

df.dropna (subset=['service','resp_bytes','orig_bytes'], axis=0  ,inplace= True)

df['orig_bytes']=df['orig_bytes'].astype('int64')
df['resp_bytes']=df['resp_bytes'].astype('int64')
df['duration']=df['duration'].astype('float64') 

#Ploting an scatter plot
plt.scatter (df['ts'],df['resp_bytes'] , marker = 'x')
plt.title('Scatter plot Time vs Response bytes')
plt.xlabel('Time')
plt.scatter (df['ts'],df['orig_bytes'])
plt.title('Scatter plot Time vs Origin bytes')
plt.ylim (0 ,700)
plt.xlim (1.575413e+09,1.575414e+09)
plt.ylabel('orig_bytes and resp_bytes')
plt.show()

test_df = df[['id_resp_p','service','duration']]
grp_df = test_df.groupby(['id_resp_p','service'], as_index= False).mean()
pivot_df = grp_df.pivot (index ='service' ,columns = 'id_resp_p') 

sns.heatmap(pivot_df,cmap = 'RdBu')

plt.show()
