# Lab 30

#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - a simple for loop"""

# for-loop is perfect for stepping through this list
iplist = ["10.1.1.1", "10.2.2.2", "10.3.3.3"]  # list of IP (str)

# 'ip' is just a variable as we step through iplist
for ip in iplist:
    print(ip)   # we indent to show this is the code we want to run each time
    # through the loop


# open file in read mode
with open("files/dnsservers.txt", "r") as dnsfile:
   # create list of lines
   #dnslist = dnsfile.readlines() 

   for svr in dnsfile:
      svr = svr.rstrip('\n')
      if svr.endswith('org'):
         with open("files/org-domain.txt", "a") as srvfile:  # 'a' is append mode
            srvfile.write(svr + "\n")
        # ELSE-IF the string svr ends with 'com'
      elif svr.endswith('com'):
         with open("files/com-domain.txt", "a") as srvfile:  # 'a' is append mode
            srvfile.write(svr + "\n")
import uuid

howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs...")

# range is required because an int cannot be looped
for rando in range(howmany):
    print( uuid.uuid4() )