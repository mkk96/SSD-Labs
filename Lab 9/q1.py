import sys
import re
input_from_cmd=sys.argv[1]
if(len(sys.argv[1])==0):
    print()
else:
    if( input_from_cmd[0].islower()):
        result=re.split("[A-Z]", input_from_cmd)
        print(result[0],end="")
    print(" ",end="")
    result = re.findall('[A-Z][^A-Z]*',input_from_cmd)
    i=0
    while(i<len(result)):
        result[i]=result[i][0].lower()+result[i][1:]
        i=i+1 
    print(' '.join(result))