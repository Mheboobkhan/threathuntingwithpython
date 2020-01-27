# This is programe to illustrate how to do pattern mathcing over history 
from collections import deque 

def search (lines, pattern, history=5):
    previous_lines = deque (maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

#Example use on file 
if __name__ == '__main__':
    file_name = input ("Enter the file name to read ::")
    with open (file_name) as f:
        S = input ("Enter the string to search ::")
        for line, prevlines in search (f, S, 5):
            for pline in prevlines:
                print (pline, end='')
                print ('-'*20)
                
