import os 
import csv


in_file = input ("Enter the Path/Name of pcap file ::")
out_file = input ("Name the output file ::")
print ('='*23)
print ('choose the extension')
exten = input  (' 1 >> .txt \n 2 >> .csv \n 3 >> .json \n')
#print (exten)
def Converter (i):
    if (i == '1'):
        os.system ('tshark -r'+in_file +'->'+ out_file +'.txt')
        print (out_file+'.txt is created')
        
    elif (i == '2'):
        print ('='*23)
        
        pcap_fields = []
        
        print ('Enetr the fields you want in csv')
        
        
        for j in range (len(pcap_fields)):
            print('[+] '+str(j)+' ' +'>>>'+' '+ pcap_fields[j])
        print ('='*23)
        print ('Or You are lazzy like me just type "DEFAULT"')
        
        Field_number = input()
        Choice = []
        for _ in range (Field_number):
            Choice.append(input())
        
        print (Choice)
        """
        os.system ('tshark -r'+in_file +'-E header=y -E separator=,'+'>'+out_file+'.csv')
        
        # TO DO :: Need to add all fields in the this 
        
        print (out_file+'.csv is created')
        """
           
    else :    
        print ('invalid extension')
Converter(exten)

#os.system ('tshark -r'+in_file +'>'+ out_file +'.txt')
#https://medium.com/hacker-toolbelt/wireshark-filters-list-983c49468a45  

