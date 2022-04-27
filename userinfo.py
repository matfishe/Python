userName = input("What is your name? ")
userAge = input("How old are you? ")
userAgeint = int(userAge)

print("Hello there " + userName)

userAgeTenTime = userAgeint * 10

print("Your age times ten is " + str(userAgeTenTime))

if (userAgeint >= 18):
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote.")
