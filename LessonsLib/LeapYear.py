def is_leap_year(year: int) -> bool:
    is_leap = (year % 400 == 0) or((year % 4 == 0) and (year % 100 != 0))
    #1
    print(f"{year}%400: {(year % 400 == 0)}")
    #2
    print(f"{year}%4: {(year % 4 == 0)}")
    3#
    print(f"{year}!%100: {(year % 100 != 0)}")

    return is_leap

print (f"2018 is leap: {is_leap_year(2018)}")  # False
#1=true;2= false;
print (f"2018 is leap: {is_leap_year(2017)}")  # False
print (f"2018 is leap: {is_leap_year(2016)}")  # False
is_leap_year(2017)  # False
is_leap_year(2016)  # True
'''
если он делится без остатка на 400
одновременно делится без остатка на 4 и не делится на 100:
'''