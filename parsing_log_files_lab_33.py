# Lab 33

#!/usr/bin/python3
# parse keystone.common.wsgi and return number of failed login attempts

loginFail = 0
loginSuccess = 0

with open("files/keystone-log.txt", "r") as logFile:
    for line in logFile:
        if "- - - - -] Authorization failed" in line:
            print("Failed IP: ", line.split(" ")[-1])
            loginFail += 1 #increment loginfail
        elif "-] Authorization failed" in line:
            loginSuccess += 1

    print(f"Total Failed: {loginFail} \nTotal Succeeded: {loginSuccess}")