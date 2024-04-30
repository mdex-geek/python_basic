year = int(input('enter your year:'))



if (year%400 ==0) or (year%4==0 and year%100 != 0):
    print('this year is leap year :',year )
else:
    print('this year this not a leap year:' , year)