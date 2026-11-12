"""
This file is a CLI demo of the pyroast package methods
"""

from pyroast import pyroast

def main():
    print("Welcome to pyroast")
    print("We have 6 different methods that take in user input and return string roast outputs")

    while True:
        print("Please select an option for roast function or quit")
        print("1: roast_gpa")
        print("2: roast_height")
        print("3: roast_sleep")
        print("4: roast_coffee")
        print("5: roast_age")
        print("6: roast_screen_time")
        print("7: quit")
        print()
        choice = input("What is your choice (please input a number): ")
        print()

        if(choice == "1"):
            print("roast_gpa is a method that roasts you based on your gpa")
            print("input your gpa as a float or integer")
            print()
            gpa = float(input("What is your gpa?: "))

            result = pyroast.roast_gpa(gpa)

            print(result)
            print()

        elif(choice == "2"):
            print("roast_height is a method that roasts you based on your height")
            print("input your height in feet as a float or integer")
            print()
            height = float(input("What is your height?: "))
        
            result = pyroast.roast_height(height)
        
            print(result)
            print()

        elif(choice == "3"):
            print("roast_sleep is a method that roasts you based on your sleep")
            print("input your number of hours of sleep as a float or integer")
            print()
            sleep = float(input("How much have you slept?: "))
                
            result = pyroast.roast_sleep(sleep)
                
            print(result)
            print()

        elif(choice == "4"):
            print("roast_coffee is a method that roasts you based on how many cups of coffee you had")
            print("input your number of cups of coffee as an integer")
            print()
            coffee = int(input("How much coffee have you had?: "))
                        
            result = pyroast.roast_coffee(coffee)
                        
            print(result)
            print()

        elif(choice == "5"):
            print("roast_age is a method that roasts you based on your age")
            print("input your age as an integer")
            print()
            age = int(input("What is your age?: "))
                                
            result = pyroast.roast_age(age)
                                
            print(result)
            print()

        elif(choice == "6"):
            print("roast_screen_time is a method that roasts you based on your screen time")
            print("input your screen time as a float or integer")
            print()
            time = float(input("What is your screen time?: "))
                                        
            result = pyroast.roast_screen_time(time)
                                        
            print(result)
            print()

        elif(choice == "7"):
            print("Thank you for checking out pyroast!")
            print()
            break

        else:
            print("That is not a valid option, please try again")
            print()

if __name__ == "__main__":
    main()