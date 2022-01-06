#!/usr/bin/env python3
######## EXPLORE READ ##########

filePath = input("path to file?")
## create file object in "r"ead mode
configfile = open(f"{filePath}", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open(f"{filePath}", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

newlist = []

## Iterate through configlist
for x in configlist:
    #print(x.strip().splitlines())
    newlist.append(x.strip().splitlines())

print(len(newlist))
## Always close your file
configfile.close()
