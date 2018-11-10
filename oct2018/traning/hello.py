
#def hello(s, y):
 #   print (s + y)

#efefew
"""frfrfrrr"""
#hello("Hello", "world")
"""comment"""

def percents (x,y):
    """What percentage of x is y"""
    one_percent = x / 100
    result = y / one_percent
    return result

def printpercents(x,y):
    """Print what percentage of x is y"""
    print(str(y)+ " is " + str(percents(x,y)) + "% of " + str(x))


printpercents(200,50)

from math import sin
print (sin(90))


from datetime import date

date_in_past = date(2000,1,15)
print (date_in_past)
print(date_in_past.weekday())
date_in_future = (date(2020,1,1)
                  