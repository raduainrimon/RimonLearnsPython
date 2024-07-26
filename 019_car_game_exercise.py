'''
Question:
Write a Python script to create a simple car control system. The program should:
Start the Car:
If the user types start, the script should start the car.
If the car is already started, print "The car is already started."
Stop the Car:
If the user types stop, the script should stop the car.
If the car is already stopped, print "The car is already stopped."
Help:
If the user types help,
print a message showing the commands start, stop, and help.
Quit:
If the user types quit, exit the program.
Unknown Command:
For any other input, print "Sorry, I don't understand!"
The script should keep running and accepting commands until the user types quit.
Make sure the program handles commands in a case-insensitive manner.
'''

#Solution
# Python script for a simple car control system
# Print an introductory message to guide the user
print("Welcome to the Car Control System!")
print("You can use the following commands:")
print("start - To start the car")
print("stop  - To stop the car")
print("help  - To show this help message")
print("quit  - To exit the program")
print()  # Print a blank line for better readability

command = "" #empty_string
started = False # Boolean variable to track whether the car is started or not
#while command.lower != "quit":
#while command != "quit":
while True:
    #command=input("> ")
    command = input("Your Command: ").lower()
    #if command.lower() == "start":
    if command == "start": # Check if the user input is 'start'
        if started: # If the car is already started
            print("car is already started")
        else: # If the car is not started
            started = True # Set the car state to started
            print("car started.. ready to go!")
    #elif command.lower() == "stop":

    elif command == "stop":  # Check if the user input is 'stop'
        if not started:  # If the car is already stopped
            print("car is already stopped")  # Inform the user that the car is already stopped
        else:  # If the car is started
            started = False  # Set the car state to stopped
            print("car stopped.")  # Inform the user that the car has stopped


    elif command == "help":
        # Print a formatted help message showing available commands
        print("""
Available Commands:
===================
start - Start the car
stop  - Stop the car
help  - Show this help message
quit  - Exit the program
        """)

    elif command == "quit":  # Check if the user input is 'quit'
        break  # Exit the loop and terminate the program

    else:  # Handle any other input that does not match the above commands
        print("Sorry, I don't understand!")