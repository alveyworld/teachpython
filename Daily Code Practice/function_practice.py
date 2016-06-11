__author__ = 'carol'
def echo(x):
    return x
def swap(x,y):
    return y,x
def revers(x):
    return -x
def plus(x,y):
    return x+y
def diff(x,y):
    return x-y
def abs_diff(x,y):
    diff = x-y
    if diff <0:
        diff = diff * -1
    return diff
def divide(x,y):
    return x/y
def remainder(x,y):
    x%y
def power(x,y):
    return x**y
def main_arithmetic():
    mystr='hello world'
    a = 2
    b = 3
    echo_ans = echo(mystr)
    print 'echo(mystr) = ',echo_ans
    a,b = swap(a,b)
    print 'swap(a,b) = ',a,b
    x=revers(6)
    print "revers(6)= ",x
    a=plus(a,10)
    print "plus(a,10) = ",a



main_arithmetic()
