import sys
import numpy as np

def main(text, *args):
    loop_list = sys.argv[1:]
    newlist = []
    
    x = list(map(int, loop_list))
        #Convert string to integer list
    y = [i for i in x]
    
    for z, i in enumerate(y):
        newlist.append(z)
        
    z = np.add(newlist, y)
    return(z)
    
    
print(list(main(sys.argv[1:])))