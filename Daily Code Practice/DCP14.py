__author__ = 'stander'
import random

def instructions():
    print "This is a game"

def roll_again(name):
    ans = 0
    while ans != 1 and ans != 2:
        ans = input("Roll Again or Pay a Fine, "+name+" (1=Roll, 2=Pay)? ")
    return ans

def roll_dice(num):
    x = random.randrange(num+1)
    y = random.randrange(num+2)
    print "You rolled a",x,"and a",y
    if x==y:
        return True
    else:
        return False

def roll_thrice(name,num):
    free = roll_dice(num)
    for i in range(2):
        if free:
            print "You get out of Jail Free"
            print "---------------------------End Turn------------------"
            return 0
        else:
            print "Better get used to these bars, "+name
        print name+", you have rolled",i+1,"times"
        roll = roll_again(name)
        if roll == 2:
            print "That will be $50 to get out of Jail"
            print "---------------------------End Turn------------------"
            return 50
        free = roll_dice(num)
    print "That will be $50 to get out of Jail"
    print "---------------------------End Turn------------------"
    return 50

def play_game(p1,p2,num):
    p1total = 0
    p2total = 0
    while p1total<200 and p2total<200:
        p1total += roll_thrice(p1,num)
        p2total += roll_thrice(p2,num)
    if p1total<p2total:
        print p1,"wins the game"
    elif p2total < p1total:
        print p2, "wins the game"
    else:
        print "It's a tie"

def main():
    instructions()
    p1 = raw_input("Enter name of first player: ")
    p2 = raw_input("Enter name of second player: ")
    dice = input("Enter the number of sides on the dice you are using: ")
    play_game(p1,p2,dice)
main()

