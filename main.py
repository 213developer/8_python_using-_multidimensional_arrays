rates = [30.00,26.00,24.00,22.00,20.00],[60.00,52.00,46.00,40.00,35.00],[88.00,70.00,67.00,60.00,50.00],[115.00,96.00,89.00,75.00,66.00],[140.00,120.00,110.00,88.00,84.00]
# Declare two dimensional list here

# Declare other variables
QUIT = 99

age = int(input("Enter the age of the child or 99 to quit: "))

# Perform a priming read to get the age of the child
while age != QUIT:
    days = int("Enter the number of days" )
    # Ask the user to enter the number of days

    # Print the weekly rate
    print("Weekly rate is: ", rates[days-1][age])
    # Ask the user to enter the next child's age
    age = int(input("Enter the age of the child or 99 to quit: "))

print("End of program")
