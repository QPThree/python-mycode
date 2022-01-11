#!/usr/bin/python3
"""Alta3 Research | <your name here>
   Using an HTTP GET to determine when the ISS will pass over head"""

# python3 -m pip install requests
import requests

import datetime

def main():
    """your code goes below here"""
    data = requests.get('http://api.open-notify.org/iss-pass.json?lat=47.6&lon=-122.3')
    print(data.json())
    # stuck? you can always write comments
    # Try describe the steps you would take manually


    for day in data.json()['response']:
        epochtime = day['risetime']
        print(epochtime)
        datetime_time = datetime.datetime.fromtimestamp(epochtime)
        print(datetime_time)


if __name__ == "__main__":
    main()
