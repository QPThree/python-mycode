#!/usr/bin/env python3

import netifaces


for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    print(netifaces.ifaddresses(i))
    print(netifaces.AF_LINK)
    print(list(netifaces.ifaddresses(i).keys())[0])


