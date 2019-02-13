#THIS IS FOR CALUCLATING MILK RATES
#CREATED  BY VERTECHX
#DATA FOR COWMILK RATES
#CHANGE THIS DATA ACCORDING TO YOUR NEEDS
datacmrates={30:24.15,31:24.76,32:24.54,33:24.79,34:24.99,35:25.20,36:25.41,37:25.62,38:25.83,39:26.04,40:26.25,41:26.46,
             42:26.67,43:26.88,44:27.09,45:27.30}
#DATA FOR BUFFELO MILK RATES
databmrates={50:30.00,51:30.60,52:31.20,53:31.80,54:32.40,55:33.00,56:3360,57:34.20,58:34.80,59:35.40,60:36.00,61:36.60,
             62:37.20,63:37.80,64:38.40,65:39.00,66:39.60,67:40.20,68:40.80,69:41.40,70:42.00,71:42.60,72:43.20,73:43.80,
             74:44.40,75:45.00,76:45.60,77:46.20,78:46.80,79:47.40,80:48.00,81:48.60,82:49.20,83:49.80,84:5040,85:51.00,
             86:51.60,87:52.20,88:52.80,89:53.40,90:54.00,91:54.60,92:55.20,93:55.80,94:56.40,95:57.00,96:57.60,97:58.20,
             98:58.80,99:59.40,100:60.00}
def cmrates():                       #CALLS CMRATES FUNCTION
    data=input("enter how many days dataavalible in numbers")
    data=int(data)
    totalmoney=0
    for i in range (0,data):
        cmday=int(input("enter your day liters"))
        cmfat=int(input("enter your day snf"))
        newcmrate=datacmrates[cmfat]
        money=cmday*newcmrate
        totalmoney=totalmoney+money
    print("THE TOTAL MONEY IS: {0}".format(totalmoney)) #THIS IS YOUR TOTAL MONEY FOR CUSTOMER

def bmrates():
    data=input("enter how many days dataavalible in numbers")
    data=int(data)
    totalmoney=0
    for i in range (0,data):
        bmday=int(input("enter your day bm liters"))
        bmfat=int(input("enter your day snf"))
        newbmrate=databmrates[bmfat]
        money=bmday*newbmrate
        print(money)
        totalmoney=totalmoney+money
    print("THE TOTAL MONEY IS: {0}".format(totalmoney))

milk=input("enter cm or bm")
if milk in ['cm','CM']:
    cmrates()   #calls cmrates function
elif milk in ['bm','BM']:
    bmrates()
else:
    exit()
