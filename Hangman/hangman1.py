import random

def get_random_guess_word():
    wordfile = "/usr/share/dict/words"
    optional_words = []
    with open(wordfile) as f:  
       for word in f:
            word= word.strip()
            if len(word) >= 6 and word.islower() and word.isalpha():
                optional_words.append(word) 
    guessed_word = random.choice(optional_words)
    # print(guessed_word)
    return guessed_word



def intro_game(guessed_word,chance_of_attempt):
    word_legth= len(guessed_word)
    print("The length of the hidden word is :",word_legth)    
    print("Your total chances to guess : ",chance_of_attempt)
    print("All The Best! Lets Start the Game!")


def check_length_of_input_word(input_word):
    length_of_input_word=len(input_word)
    while True:
        if(length_of_input_word>1):
            input_word = input("Please enter only a letter! : ") 
            length_of_input_word=len(input_word)
        elif(length_of_input_word==0):
            input_word = input("Please enter a letter : ") 
            length_of_input_word=len(input_word)
        else:
            break
    return input_word

def repeat_rounds(guessed_word,users_word,chance_of_attempt):
    input_word = input("Enter a letter : ") 
    single_input_word=check_length_of_input_word(input_word)
    # print(single_input_word)
    is_word=False
    for index,word in enumerate(guessed_word) :
        if(word==single_input_word):
            is_word=True
            users_word[index]=single_input_word



    if(is_word==False):
        print("Oops!!! Wrong Guess!")
        chance_of_attempt-=1
    
    return chance_of_attempt

   

def play_game():
    users_word=[]
    guessed_word = get_random_guess_word()
    chance_of_attempt=6
    print(guessed_word)
    for word in guessed_word:
        users_word.append("_")
    # print(users_word)
    intro_game(guessed_word,chance_of_attempt)
    while True:
        chance_of_attempt= repeat_rounds(guessed_word,users_word,chance_of_attempt)
        print("User Word :",users_word)
        print("Remaining Chances :",chance_of_attempt)
        print("--------------------------------------------------------")
        if(chance_of_attempt==0):
            print("OOOPZZZ!!!!    You Lose the game")
            break
        if("_" not in users_word):
            print("WOOOWWW!!!!    You Won the game")
            break
    

# play_game()