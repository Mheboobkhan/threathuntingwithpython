from pcapfile import savefile
from pcapfile.protocols.linklayer import ethernet
from pcapfile.protocols.network import ip
import binascii
import sys
from tempfile import TemporaryFile
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#Reading the pcap file
in_pcap = input ("Enter the file name/path ::")
test_pcap = open(in_pcap,'rb')
capfile = savefile.load_savefile(test_pcap, verbose = True)

#Converting pcap file in .txt and storing in data variable, using TemporaryFile
print ("="*23) 
with TemporaryFile('w+t') as f:
    for i in range (len(capfile.packets)):
         print ((ip.IP(binascii.unhexlify(ethernet.Ethernet (capfile.packets[i].raw()).payload))), file=f)
    f.seek(0)
    raw_data = f.read()

data = raw_data.split()
num = np.array(data)
reshaped = num.reshape(len(capfile.packets),9)
Dataset = pd.DataFrame(reshaped, columns = ['Protocol','Packets','Src','Src_IP','To','Dest_IP','Carrying','Size','Unit'])
print (Dataset)

# Lets start analysis
# Number of the IP's in the the transaction 

# Lets start analysis
# Number of the IP's in the the transaction 
print ("="*23)
print ("Below are the IP's involved in this pcap")
print (" ")
print (Dataset.Src_IP.unique())
#Printing the Maximum number of bytes transferred
print ("="*23)
print ("Maximum "+Dataset['Size'].max()+" bytes are transfers in single session") # This Data is questionable
print ("="*23)
#Ploting Graph of the Data size for beaconing anlysis 
plt.plot (Dataset['Size'])
plt.show()
