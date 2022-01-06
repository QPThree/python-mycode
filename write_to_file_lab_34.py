#Lab 34

import csv
#!/usr/bin/env python3
# outFile = open("files/admin.rc", "a")
# osAUTH = input("What is the OS_AUTH_URL? ")
# print("export OS_AUTH_URL=" + osAUTH, file=outFile)

# print("export OS_IDENTITY_API_VERSION=3", file=outFile)

# osPROJ = input("What is the OS_PROJECT_NAME? ")
# print("export OS_PROJECT_NAME=" + osPROJ, file=outFile)

# osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME? ")
# print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile)

# osUSER = input("What is the OS_USERNAME? ")
# print("export OS_USERNAME=" + osUSER, file=outFile)

# osUSERDOM = input("What is the OS_USER_DOMAIN_NAME? ")
# print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile)

# osPASS = input("What is the OS_PASSWORD? ")
# print("export OS_PASSWORD=" + osPASS, file=outFile)
# outFile.close()

with open("files/csv_users.txt") as csvFile:
    i = 0
    for row in csv.reader(csvFile):
        i = i + 1
        filename = f"files/logins/admin.rc{i}"
        with open(filename, "w") as rcfile:
            print("export OS_AUTH_URL=" + row[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
            print("export OS_USERNAME=" + row[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
            print("export OS_PASSWORD=" + row[5], file=rcfile)
print("admin.rc files created!")