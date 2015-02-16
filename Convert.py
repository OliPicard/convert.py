__author__ = 'OliPicard'
import sys
import math

#Conversions Calculator created by OliPicard after reviewing some old Python 2 code online.
#Big thanks to the original stackoverflow article that inspired me. http://stackoverflow.com/questions/14228824/python-conversion-calculator-loop-code-efficiency


#Define the Menu
def menu():
    print("-" * 25)
    print("\n Digital / Conversion Calculator by \n OliPicard \n full source code @ github.com/olipicard ")
    print("-" * 25)
    print("1. Kilobytes to Gigabytes\n")
    print("2. MegaBytes to Gigabytes\n")
    print("3. Gigabytes to MegaBytes\n")
    print ("4. Quit\n")
    print ("-" * 25)
    print ("\n")

#KBs to Gigabytes
def kilobytes_to_gigabytes(a):
    b = 1.19209289551E-7
    c = a * b
    return (a,float (c))

#GB to KBs.
def gigabytes_to_kilobytes(a):
    b = 1.19209289551E-7
    c = a / b
    return (a, float (c))

#MBs to Gigabytes
def megabytes_to_gigabytes(a):
    b = 1024
    c = a / b
    return (a, float (c))
#Gigabytes to MBs
def gigabytes_to_megabytes(a):
    b = 1024
    c = a * b
    return (a, float (c))


#check the inputs!
def check_input(user_input):
    try:
        converted_number = float (user_input)
    except ValueError:
        return -1
    return converted_number

#Program begins
loop = True
while loop:
    menu()
    choice = int(input("Choose your option: "))
    if choice not in [1,2,3,4]:
        print(choice, " is not a vaild input. please try again.")
        menu()
        choice = int(input("Pick a conversion."))

    if choice == 1:
        print("Please enter the kilobytes you wish to convert to Gigabytes.")
        kilobytes = check_input(input("Kilobytes: "))
        result = kilobytes_to_gigabytes(kilobytes)
        print('{} kilobytes = gigabytes {}'.format(*result))

    if choice == 2:
        print("Please enter the Megabytes you wish to convert to Gigabytes")
        megabytes = check_input(input("Megabytes: "))
        result = megabytes_to_gigabytes(megabytes)
        print('{} megabytes = gigabytes {}'.format(*result))

    if choice == 3:
        print("Please enter the Gigabytes you wish to convert to Megabytes.")
        gigabytes = check_input(input("Gigabytes: "))
        result = gigabytes_to_megabytes(gigabytes)
        print('{} gigabytes = megabytes {}'.format(*result))


    if choice == 4:
        loop = False

print("\n")
print ("-", 25)
print ("Thanks for using Convert.py. I hope it has proven to be useful.")