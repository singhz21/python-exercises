#This file runs an Inches to Centimetres converter program

#Define the program that will be the converter
def convert():
    #Run the program whilst checking for any errors
    try:
        #Set the constant used for conversion
        constant = 2.54

        #Inform user about the program
        print ('Hello there! I am a tiny little program that converts a value from inches to centimeters.')
        print (' ')

        #Ask user for a number
        number = input ("Please enter value in inches >>> ")
        print (' ')

        #Convert string to float value
        number = float(number)

        #Perform the conversion and set values to be strings
        result = number * constant
        number = str(number)
        result = str(result)

        #Save the result in a string
        output = number + " inches is " + result + " centimeters"

        #Print the result
        print(output)
        print (' ')

    #Run this bit of code if an error is encountered    
    except ValueError:
        print("Please enter a numeric value!")

#Call the program to be executed when the file is run
convert()
input ('Press Enter to exit ')
