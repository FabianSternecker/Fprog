import sys
import os
import time
directory = sys.argv[1]

for file in os.listdir(directory):
    if(time.time()-120<=os.path.getmtime(file)):
        print(directory + os.path.sep + file + " " +str(time.ctime(os.path.getmtime(file))))

