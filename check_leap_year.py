# year = int(input("Enter year\n>>>"))


# if (year % 4) == 0:
#     if (year % 100) == 0:
#         if (year % 400) == 0:
#             print(str(year) + ' ' + 'is leap year.')
#         else:
#            print(str(year) + ' ' + 'is not leap year.')
#     else:
#        print(str(year) + ' ' + 'is not leap year.')
# else:
#     print(str(year) + ' ' + 'is not leap year.')


year = int(input("enter the year you want to check\n>>>"))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(str(year)+ ' ' + "is leap year.")
        else:
            print(str(year)+ ' ' + "is not leap year.")
    else:
        print(str(year)+ ' ' + "is not leap year.")
else:
    print(str(year)+ ' ' + "is not leap year.")



