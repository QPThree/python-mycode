#!/usr/bin/python3

import requests
import json

# define the URL we want to use
GETURL = "http://time.jsontest.com/"
IPURL = "http://ip.jsontest.com/"

def main():
 

    # use requests library to send an HTTP GET
    resp = requests.get(f"{GETURL}")

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Todays date: {respjson['date']}\nTime Now: {respjson['time']}")

    resp = requests.get(f"{IPURL}").json()

    print(f"Your IP : {resp['ip']}")

if __name__ == "__main__":
    main()

