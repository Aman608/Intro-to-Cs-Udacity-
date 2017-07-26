days = [31,28,31,30,31,30,31,31,30,31,30,31]

def isLeapYear(y):
    if y%400==0:
        return True
    elif y%100==0:
        return False
    elif y%4==0:
        return True
    else:
        return False
def daysInMonth(y,m):
    if isLeapYear(y) and m==2:
        return days[1]+1
    return days[m-1]

def is_before(y1,m1,d1,y2,m2,d2):
    if y1 > y2:
        return False
    if y1 < y2:
        return True
    else:
        if m1<m2:
            return True
        elif d1 < d2:
            return True
        else: return False
def daysBetweenDates(y1,m1,d1,y2,m2,d2):
    d = 0
    assert not is_before(y2,m2,d2,y1,m1,d1)
    while m1<m2 or y1<y2:
        d += daysInMonth(y1,m1)
        if m1<12:
            m1+=1
        else:
            m1=1
            y1+=1
    return d - d1 + d2
