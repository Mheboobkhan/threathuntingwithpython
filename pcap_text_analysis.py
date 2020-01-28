#Data sanitization with python

#Firstly i would like to if there are URL's in the data sample
from pcapfile import savefile
from pcapfile.protocols.linklayer import ethernet
from pcapfile.protocols.network import ip
import binascii
import sys

in_pcap = input ("Enter the file name/path ::")
test_pcap = open(in_pcap,'rb')
capfile = savefile.load_savefile(test_pcap, verbose = True)

#Now capfile file will be traeted as the normal file input for python
# Store data in normal decoded format  
# 2019-12-25-traffic-analysis-exercise.pcap  File to refer 

#(ip.IP(binascii.unhexlify(ethernet.Ethernet (capfile.packets[0].raw()).payload))) This is a payload for raw file 

data = []
for i in range (len(capfile.packets)):
    data.append((ip.IP(binascii.unhexlify(ethernet.Ethernet (capfile.packets[i].raw()).payload))))
    
#Now lets create new file with all logs as strigs 

print ("="*23)
with open('out.txt', 'w') as f:
    for i in range (len(data)):
        print (data[i], file=f)
print ("out.txt is created")
print ("="*23)


