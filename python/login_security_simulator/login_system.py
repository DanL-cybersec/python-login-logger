#Create a log file that scans through the attempted passwords by the user
#Displays the attempt count

#Program alerts the rightful user of the "hacker" attempting to login in

correctPassword = input(str("Choose a password "))
attemptCount = 0
maxAttempts = int(input("How many attempts would you like to allow? "))
#Need to set the amounts we already know are necessary before the entire code so that there is a no confusion


while attemptCount < maxAttempts:
    attempt = str(input("What is your Password? "))

    if attempt == correctPassword:
        print("Welcome")
        break
        #"break" stops the loops immediately
    else:
        attemptCount += 1
        #We want to have the attempt count updated as soon as the code is ran and failed
        print("Incorrect Password")

if attemptCount == maxAttempts:
    print("Access Denied. Exceeded password limitations.")
