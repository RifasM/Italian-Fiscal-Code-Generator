#### Authors - Richard, Mukul
#### Date - 04/11/2019


import string
import re
import sys


# The following function Code4 generates the 3 character code for name and surname.
#
# It accepts the following two parameters
#      1. name (data type = String) -> The name or the surname of the user
#      2. flag (data type = String) ->
#                                   flag is set to false for name
#                                   flag is set to true for surname
#
# The output is the "sub_code" (data type = String) -> variable which consists of 3 Uppercase character code corresponding
#                                to the name or surname

def Fiscal_Code(name, flag):
    if name == "*_*":
        return 'XXX'
    # converting all characters to uppercase
    name = name.upper()

    # stores the code generated at each step
    sub_code = ""

    vowels = ['A', 'E', 'I', 'O', 'U']
    vowel_list = []

    threshold = 0  # maximum number of characters in the sub_code

    for character in name:

        # terminates the loop when threshols == 3
        if (threshold == 4):
            break

            # stores the encountered vowel in the array
        elif character in vowels:
            vowel_list.append(character)

        # stores the encountered consonant in the array
        else:
            # if(not flag and threshold==1):
            #    continue

            sub_code += character
            threshold += 1

    iterator = 0

    # removing the 2nd character or the last character
    if (threshold == 4):

        if (flag):
            sub_code = sub_code[:3]
        else:
            sub_code = sub_code[:1] + sub_code[2:]
        return sub_code

    vowel_list += 3 * ['X']

    # for appending vowels and X's
    while (threshold < 3 and iterator < len(vowel_list)):
        sub_code += vowel_list[iterator]
        iterator += 1
        threshold += 1

    return sub_code


# The following function Birthday_code generates the 5 character code on the basis of Date of Birth and gender.
#
# It accepts the following two parameters
#      1. date (data type -> String) -> The Date_of_birth in the format DD/MM/YYYY
#
#      2. Gender (data type -> String)-> M followed any string == Male
#                                        F Followed by any string == Female
#
#
# The output is the "sub_code" (data type = String) -> variable which consists of 5 Uppercase character code

def Birthday_code(date, gender):
    sub_code = ""
    gender = gender.upper()

    # delimiter used /
    day, month, year = date.split('/')

    sub_code += year[-2:]

    # fiscal codes for months
    month_table = {'01': 'A', '02': 'B', '03': 'C', '04': 'D', '05': 'E', '06': 'H', '07': 'L', '08': 'M', '09': 'P',
                   '10': 'R', '11': 'S', '12': 'T'}

    sub_code += month_table[month]

    # verifying the gender
    if bool(re.match('M.*', gender)):
        sub_code += day
    elif bool(re.match('F.*', gender)):
        sub_code += str(int(day) + 40)
    else:
        pass

    return sub_code


# Main function, receives im


if __name__ == "__main__":
    argumentList = sys.argv
    name = argumentList[1]
    surname = argumentList[2]
    gender = argumentList[3]
    date = argumentList[4]

    # resultant_code is the placeholder for the final 11 character code
    resultant_code = ""

    # call to generate surname code
    resultant_code += Fiscal_Code(surname, True)

    # call to generate name code
    resultant_code += Fiscal_Code(name, False)

    # call to generate date_of_birth code
    resultant_code += Birthday_code(date, gender)

    print(resultant_code)