import sys
import os
if len(sys.argv)<3:
    print ("Not sufficiant argument")
    sys.exit(1)

if len(sys.argv)>1:
    file_name=sys.argv[1]
    if not os.path.isfile(file_name):
        if sys.argv[2]=="-a":
             with open(file_name,'a') as f:
                option=sys.argv[2]
                print("file created")
                f.write(sys.argv[3])
