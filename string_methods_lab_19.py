def main():
   trek = "ncc 1701-d"
   a = "the prime directive"
   a = a.split(" ") # a is converted to a list of strings
   print(a)
   a = "-".join(a) # is the result of using "-" to glue together a list of string
   print(a)

main()