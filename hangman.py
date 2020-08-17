def hangman():
    import random

#Default Setting
    words = ["cat","dog","sphynx","crocodile","lama","bear","deer","salmon"]
    word = words[random.randint(0,7)]
    wrong = 0
    stages = ["",
              "_______       ",
              "I             ",
              "I      I      ",
              "I      0      ",
              "I     /II     ",
              "I     / I     ",
              "I             ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

#Game
    while wrong < len(stages) - 1:
    #Guess
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
    #Right
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'            
        #Win
            if "_" not in board:
                print("You win!!")
                print(" ".join(board))
                win = True
                break
    #Wrong
        else:
            wrong += 1
            print(" ".join(board))
            e = wrong + 1
            print("\n".join(stages[0:e]))

#Lose
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("You lose, the answer was {}.".format(word))

hangman()

