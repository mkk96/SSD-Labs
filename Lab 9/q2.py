import sys

input_from_user=sys.argv[1]
try:
    decimal=int(input_from_user,2)
    temp=decimal
    rev=0
    while(temp>0):
        dig=temp%10
        rev=rev*10+dig
        temp=temp//10
    if(decimal==rev):
        print("TRUE")
    else:
        print("FALSE")
except:
    print("TRUE")