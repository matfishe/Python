#using print function to print to file
fileobject = open("output.txt", mode="w")

print("Hello Matt", file=fileobject)

#using sep to replace space between words with a colon
print("hello","Matt","ThirdValue",sep=":")

#using end to change newline to no newline
print("hello",end="")
print("goodbye")

#using both sep and end. one can come before or after but objects like "Hello" must be first
print("hello","Matt","ThirdValue",sep=":",end="")
print("Matt")