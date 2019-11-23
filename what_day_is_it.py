# States the day of the date entered
# Only works post year 1581

def IsYearLeap(year):
    if year > 1581:
        if (year %4 == 0 and year %100 != 0) or year %400 == 0:
            return True
    else:
        return False

def DaysInMonth(year,month):
    bigmonths = [1,3,5,7,8,10,12]
    smallmonths = [4,6,9,11]
    if month in bigmonths:
        return 31
    elif month in smallmonths:
        return 30
    else: # for Feb
        if IsYearLeap(year):
            return 29
        else:
            return 28

def DayOfYear(year,month,day):
    bigmonths = [1,3,5,7,8,10,12]
    smallmonths = [4,6,9,11]
    counter = 0
    for y in range(1582,year):
        if IsYearLeap(y):
            counter += 366
        else:
            counter += 365
    for m in range(1,month):
        if m in bigmonths:
            counter += 31
        elif m in smallmonths:
            counter += 30
        elif m == 2:
            if IsYearLeap(year):
                counter += 29
            else:
                counter += 28
    counter += day
    print(counter)

    if counter % 7 == 6:
        return 'Saturday'
    elif counter % 7 == 0:
        return 'Sunday'
    elif counter % 7 == 1:
        return 'Monday'
    elif counter % 7 == 2:
        return 'Tueday'
    elif counter % 7 == 3:
        return 'Wednesday'
    elif counter % 7 == 4:
        return 'Thursday'
    elif counter % 7 == 5:
        return 'Friday'

def userinput():
    x = int(input('Select Year: '))
    y = int(input('select month: '))
    z = int(input('select day: '))
    return [x,y,z]

print(DayOfYear(2000,12,31)) # Sun
print(DayOfYear(2017,6,14)) # Wed
print(DayOfYear(1582,1,1)) # Mon
print(DayOfYear(1583,12,31)) # Tue

sel = userinput()
result = DayOfYear(sel[0],sel[1],sel[2])
print(result)