my_list = ["192.168.0.5", 5060, "UP"] #create a list

print("The first item in the list (IP): " + my_list[0] ) #Indexed still start at 0

print("The second item in the list (port): " + str(my_list[1]) ) #second item accessed at index 1

print("The last item in the list (state): " + my_list[2] ) #and so on



#Challenge: display only IP addresss on the screen
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print(iplist[3], iplist[4])