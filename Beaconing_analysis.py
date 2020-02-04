#DNS analysis
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
#Importing the DNS log file 
#Below command is  used to generate this fle 
"""
tshark  -r 2019-12-03-traffic-analysis-exercise.pcap  -T fields -E header=y -E separator=, -e ip.src -e ip.dst -e udp.dstport -e ip.len -e frame.time_delta_displayed udp.dstport==53 |sort -nk 5 -r  >> dns.csv
"""
#Importing dataset 
in_file = input ("Enter the path of the .csv file ::")
dataset = pd.read_csv(in_file)
#dataset = pd.read_csv('/home/wh/Desktop/logfiles/csv/dns.csv')
dataset.plot(x='frame.time_delta_displayed',y='ip.len',style ='o')
plt.show()
