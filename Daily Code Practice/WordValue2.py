__author__ = 'stander'
def main_from_user():
    answer = 'start'
    while answer == 'y':
        myword = raw_input("Enter a word to get the value of: ")
        print "The value of",myword,"is",getWordValue(myword)
        answer=menu()

def main(): #from file
    fin = open("american-english.txt","r")
    for word in fin:
        word = word.strip()
        if getWordValue(word)==100:
            print word
    fin.close()


def getWordValue(word):
    total = 0
    for char in word:
        v = ord(char)-ord('a')+1
        total = total + v
    return total

def menu():
    ans = 'start'
    while ans != 'y' and ans != 'n':
        ans = raw_input('Do you wish to continue? (y/n)')
    return ans
main()
