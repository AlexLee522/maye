#-*-coding:utf-8-*-
import sys
def IsLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 :
        return True
    elif year % 400 == 0 :
        return True
    else:
        return False

def GetNumOfTheMonth(year,month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif IsLeapYear(year):
        return 29
    else:
        return 28

def GetTotalDay(year,month):
    day = 0
    for i in range(1970,year):
        if IsLeapYear(i) :
            day += 366
        elif IsLeapYear(i) == False:
            day += 365
    if IsLeapYear(year) == True:
        ms = [31,29,31,30,31,30,31,31,30,31,30,31]
    elif IsLeapYear(year) == False:
        ms = [31,28,31,30,31,30,31,31,30,31,30,31]
    for j in range(0,13):
        if j+1 < month :
            day +=  ms[j]
    return day

def GetStartDay(year,month):
    x = 4 + GetTotalDay(year,month) % 7
    if x > 7 :
        x = x - 7
    elif x < 7 or x == 7 :
        x = x
    return x

month_dict = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

def MonthName(month):
    return month_dict[month]

def PrintTitle(year,month):
    print '           %d,%s'%(year,MonthName(month))
    print '-------------------------------------'
    print '  Sun  Mon  Tue  Wed  Thu  Fri  Sat  '

def PrintBody(year,month):
    p = GetStartDay(year,month) 
    if p != 7 :
        sys.stdout.write(' '*5*p)
    for j in range(1,GetNumOfTheMonth(year,month)+1):
        print '%4d'%j,
        p += 1
        if p % 7 == 0 :
            print '   '

year = int(raw_input('please input the year:'))
month = int(raw_input('please input the month:'))
PrintTitle(year,month)
PrintBody(year,month)



