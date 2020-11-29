# Programmer    - Sean Michaels
# Date          - November 28th, 2020
# Purpose       - UiT Masters in Computer Science required coding project
# Python Version- 3.8.2
# Version       - Version 1.0
# Last Edited   - 11/28/2020
# Description   - Converts integers to roman numerals, and roman numerals to integers

romans =    {'M':1000, 'CM':900, 'D':500, 'CD':400,             # key value pairs of roman numerals
            'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10,
            'IX':9, 'V':5, 'IV':4, 'I':1}

# Convert integer from 1-3999 to roman numeral
def int_to_roman(num):
    values = list(romans.values())
    symbols = list(romans.keys())
    roman = ''
    i = 0                                                       # start at largest number
    while num > 0 and num < 4000:                               # constraints of project
        for j in range(num // values[i]):                       # floor division of given number
            roman += symbols[i]                                 # append symbol to answer
            num -= values[i]                                    # remove place value
        i+=1                                                    # increment through place value

    return roman

# Convert roman numeral I to MMMCMXCIX
def roman_to_int(st):
    int_value = 0
    for i in range(len(st)):
        if i > 0 and romans[st[i]] > romans[st[i - 1]]:         # check for subtraction notation
            int_value += romans[st[i]] - 2 * romans[st[i - 1]]  # account for subtraction notation
        else:                                                   # total + (current-2*previous) then add to total
            int_value += romans[st[i]]                          # add conversion to total
    return int_value                                            # return converted integer

# Convert 1-3999 to roman numeral and print
#  convert roman numeral back to integer and print
def all_vals(max_val):
    roms = []
    vals = []
    for i in range(max_val):                                    # loop through 1-3999
        roms.insert(i, int_to_roman(i))                         # convert to roman numeral and write to list

    print('Converted Roman Numerals: ')
    for items in roms:
        print(items)                                            # print converted roman numerals list

    for items in roms:
        vals.append(roman_to_int(items))                        # convert roms list to list of integers

    print('Converted Integers: ')
    for items in vals:                                          # print converted integers list
        print(items)

# main function to handle user input and function calls
def main():
    user_val = input("Enter a value: ")                         # get user input
    if user_val.isalpha():                                      # make sure input is string values
        print("Your value is: " + str(roman_to_int(user_val)))
    elif user_val.isnumeric():                                  # make sure input is a numeric value
        val = int(user_val)
        print("Your roman numeral is: " + int_to_roman(val))
    else:
        print("Sorry value " + user_val +
                " is not a roman numeral or an integer")

    user_val = input("See all roman numerals and integers? y = yes, n = no: ")
    if user_val == 'y':                                         # check if all possible conversions is wanted by the user
        all_vals(4000)                                          # max value limit given

# ----------- Main Program Begin ------------
if __name__ == "__main__":
    main()                                                      # main program call
