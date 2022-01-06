#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   learning about for logic"""

# create the list called vendors
vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]

# loop across the list vendors
for x in vendors:
    print("\nThe vendor is " + x, end="") # each time through the loop print value of x
    if x not in approved_vendors:   # if x does not appear within the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.")  # when the loop ends print this

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
for farm in farms:
    print(f"{farm['name']} : {farm['agriculture']}")