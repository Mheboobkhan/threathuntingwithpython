file_name = input ("Enter the name of file ::")
fopen =open(file_name)
md5file = open("MD5.txt" , 'w+')
sha1file = open ("sha1.txt", 'w+')
sha256file = open ("sha256.txt",'w+')
for line in fopen:
    l = line.split()
    #print (l)
    #condition to neglect null list
    if len(l) == 0:
        print ('----')
    else:
        for i in range (len(l)) :
            if (len(l[i])== 32):
                md5file.write(l[i]+'\n')
                print('MD5')
            if (len(l[i])== 40):
                sha1file.write(l[i]+'\n')
                print('sha1')
            if (len(l[i])== 64):
                sha256file.write(l[i]+'\n')
                print('sha256')
                
                    
fopen.close()
md5file.close()
sha1file.close()
sha256file.close()

            
            
    
    


    

