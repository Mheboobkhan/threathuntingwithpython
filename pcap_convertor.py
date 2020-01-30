import os 
import csv
in_file = input ("Enter the Path/Name of pcap file ::")
out_file = input ("Name the output file ::")
print ('='*23)
print ('choose the extension')
exten = input  (' 1 >> .txt \n 2 >> .csv \n 3 >> .json \n')

def Converter (i):
    if (i == 1):
        os.system ('tshark -r'+in_file +'>'+ out_file +'.txt')
        print (out_file+'.txt is created')
           
    else :    
        print ('invalid extension')

Converter(exten)

#os.system ('tshark -r'+in_file +'>'+ out_file +'.txt')


