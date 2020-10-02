import pandas as pd 
import numpy as np 
import matplotlib  as plt 

dataset  = pd.read('test2.csv')
dataset.plot (x='farme.time_relative', y='frame.len',style='x')
plt.show ()
