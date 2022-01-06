#!/usr/bin/env python3
######## EXPLORE READ ##########

file = input("path to file?")
## create file object in "r"ead mode
configfile = open(f"{file}", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open(f"{file}", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

newlist = []

## Iterate through configlist
for x in configlist:
    pass
    #print(x.strip().splitlines())
    newlist.append(x.strip().splitlines())

print(len(newlist))
## Always close your file
configfile.close()
