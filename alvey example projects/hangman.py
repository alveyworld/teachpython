import random

def get_words():
    fin = open("words.txt", "rb")
    words = []
    for line in fin:
        line = line.strip()
        words.append(line)
    fin.close()
    return words

def pick_word(words):
    # Pick a random word
    num = random.randrange(len(words))
    return words[num]

def new_game(words):
    guessed_letters = []
    word = pick_word(words)
    misses = 0
    game = [ guessed_letters, word, misses ]
    return game

def is_word_guessed(game):
    guessed_letters = game[0]
    word = game[1]
    # return True if all letters have been guessed.
    # otherwise return False
    for j in range(len(word)):
        found = False
        for i in range(len(guessed_letters)):
            if word[j] == guessed_letters[i]:
                found = True
                break
        if not found:
            return False
            
    return True

def is_game_over(game):
    misses = game[2]
    # return True if too many guesses, or word has been guessed.
    if misses >= 6:
        return True
    if is_word_guessed(game):
        return True
    return False

def guess_letter(game, letter):
    game[0].append(letter)
    #if the letter is in the word?
    if not letter in game[1]:
    	game[2]+=1
    return game

def display_picture(game):
    misses = game[2]
    if misses > 0:
        print " O "
        
    if misses == 2:
        print " | "
    elif misses == 3:
        print "/| "
    elif misses >= 4:
        print "/|\\"

    if misses == 5:
        print "/  "
    elif misses >= 6:
        print "/ \\"
    return


def display_word(game):
    print game[1]
    return

def display_guessed_letters(game):
    print game[0]
    return

def display_status(game):
    display_picture(game)
    print
    display_word(game)
    print
    display_guessed_letters(game)
    print
    print
    return

def main():
    words = get_words() #get long list of words
    game = new_game(words) #get a list with the game data  list, string, int
    display_status(game)
    while not is_game_over(game):
        guess = raw_input("next guess? ")
        guess = guess.strip()
        if len(guess) > 0:
            guess = guess.lower()
            game = guess_letter(game, guess[0])
        display_status(game)

    if not is_word_guessed(game):
        print "The word is:", game[1]
        print ""
        
    return

if __name__ == "__main__":
    main()