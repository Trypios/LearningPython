def numberToWords(number):
    '''Converts Integers to their text representation e.g. 1019 to One Zero One Nine'''

    str_number = str(number)
    str_number_result = ''
    if number < 0:
        print("The number {} is negative. \nThis program only works with positive numbers. \nTake your negativity elsewhere...\n".format(number))
        return -1
    for char in str_number:
        if char=="1":
            str_number_result += "One "
        elif char=="2":
            str_number_result += "Two "
        elif char=="3":
            str_number_result += "Three "
        elif char=="4":
            str_number_result += "Four "
        elif char=="5":
            str_number_result += "Five "
        elif char=="6":
            str_number_result += "Six "
        elif char=="7":
            str_number_result += "Seven "
        elif char=="8":
            str_number_result += "Eight "
        elif char=="9":
            str_number_result += "Nine "
        elif char=="0":
            str_number_result += "Zero "
        else:
            print("Invalid character")
    print("The number '{}' in text form is: {}\n".format(number, str_number_result))

# TESTING:
numberToWords(123)
numberToWords(1010)
numberToWords(1000)
numberToWords(-12)
numberToWords(0)
numberToWords(2)