import sys
import re
List=re.split(" ",sys.argv[1])
if(len(sys.argv[1])==0):
    print("[]")
else:
    intList=[]
    try:
        for i in List:
            intList.append(int(i))
    except:
        intList.clear()
        for i in List:
            intList.append(float(i))
    intList.sort(key=lambda x:x)
    print(intList)