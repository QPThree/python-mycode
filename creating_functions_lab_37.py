#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import json
import crayons

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {crayons.green("ip")}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to send command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

# start our main script
def main():
    """called at runtime"""

    with open("files/devicemd.json") as devicemdfile:
        # dict containing IPs mapped to a list of physical interfaces and their state
        devicecmd = json.load(devicemdfile)

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

# call our main function
main()
