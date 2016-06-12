# Zack Alvey example program
# Program to guess the user's number from 1 to 1000
# in 10 guesses or fewer.
# Illustrates how to combine the concepts of 
# decisions (if), loops (while), variables, and 
# arithmetic & relational operators

def main():
	print "Pick a number 1-1000, don't tell me."
	print "I will guess it in 10 tries or less."
	print "enter 0 if I get it right"
	print "enter -1 if I need to lower"
	print "enter 1 if I need to go higher"
	
	high = 1000
	low = 1
	tries = 1
	
	while high > low:
		avg = (high + low)/2
		print "My guess is ", avg
		feedback = input("Please enter -1, 0, or 1: ")
		if feedback == 0:
			print "That took", tries, "guesses."
		elif feedback == -1:
			if avg - 1 >= low:
				high = avg -1
				tries = tries + 1
			else:
				print "not possible, you cheated"
		elif feedback == 1:
			if avg +1 <= high:
				low = avg + 1
				tries = tries + 1
			else:
				print "not possible, you cheated"
		else:
			print "please only enter -1, 0, or 1"
		

if __name__ == "__main__":
	main()



