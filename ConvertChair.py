__author__ = 'OliPicard'
import sys
import math

#Conversions Calculator created by OliPicard after reviewing some old Python 2 code online.
#Refactored & updated with Digital Unit conversions
#If you experience any bugs/problems open a ticket on github.com/olipicard/convert.py
#Full Credits at github.com/olipicard/convert.py


#Define the Menu
def menu():
    print("-" * 25)
    print"\n Digital / Conversion Calculator by \n OliPicard \n full source code @ http://github.com/olipicard "
    print"-" * 25
    print"1. Kilobytes to Gigabytes\n"
    print"2. MegaBytes to Gigabytes\n"
    print"3. Gigabytes to MegaBytes\n"
    print"4. Gigabytes to Kilobytes\n"
    print"5. Quit\n"
    print("-" * 25)
    print"\n"

#KBs to Gigabytes
def kilobytes_to_gigabytes(a):
    b = 1048576
    c = a / b
    return (a,float (c))

#GB to KBs.
def gigabytes_to_kilobytes(a):
    b = 1048576
    c = a * b
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
    choice = int(raw_input("Choose your option: "))
    if choice not in [1,2,3,4,5]:
        print(choice, " is not a vaild input. please try again.")
        menu()
        choice = int(raw_input("Pick a conversion."))

    if choice == 1:
        print("Please enter the kilobytes you wish to convert to Gigabytes.")
        kilobytes = check_input(raw_input("Kilobytes: "))
        result = kilobytes_to_gigabytes(kilobytes)
        print('{} kilobytes = gigabytes {}'.format(*result))

    if choice == 2:
        print("Please enter the Megabytes you wish to convert to Gigabytes.")
        megabytes = check_input(raw_input("Megabytes: "))
        result = megabytes_to_gigabytes(megabytes)
        print('{} megabytes = gigabytes {}'.format(*result))

    if choice == 3:
        print("Please enter the Gigabytes you wish to convert to Megabytes.")
        gigabytes = check_input(raw_input("Gigabytes: "))
        result = gigabytes_to_megabytes(gigabytes)
        print('{} gigabytes = megabytes {}'.format(*result))

    if choice == 4:
        print("Please enter the Gigabytes you wish to convert to kilobytes.")
        gigabytes = check_input(raw_input("Gigabytes: "))
        result = gigabytes_to_kilobytes((gigabytes))
        print('{} gigabytes = kilobytes {}'.format(*result))

    if choice == 5:
        loop = False

print"\n"
print "-", 25
print "Thanks for using Convert.py. I hope it has proven to be useful."
print "If you experienced any bugs, feel free to report them at http://github.com/olipicard/Convert.py"
