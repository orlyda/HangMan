import random


def the_game(mistake, word):
    word = word.replace("\n", "")
    end = bool(mistake > 0)
    length=len(word)
    while end & (length > 0):
        l = input("Insert a letter: ")
        if len(l) != 1:
            assert Exception("You've inserted more the one letter")
        if l in word:
            print("Great, you are right")
            word.replace(l, "")
            length=length-1
        else:
            print("This letter doesn't occur")
            mistake = mistake - 1
            print("You have " + str(mistake) + " tries")
        end = bool(mistake > 0)

    if length == 0:
       print("Good job, you guessed the word")
    else:
       print("Sorry, you finished all your tries")


word = open("words.txt", "r")
x = word.readlines()
choose = random.randint(1, len(x))  # choose randomly word from the 'words' file
the_chosen_word = x[choose - 1]
mistake = int(input("How much tries do you want to have? "))
the_game(mistake, the_chosen_word)
