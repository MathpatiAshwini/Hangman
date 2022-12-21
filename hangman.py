import random
def hangman():
    words=['ashwini','laptop','topper','girl','india']
    word1=random.choice(words)
    turns= 10
    guessmade= ''
    valid=set('abcdefghijklmnopqrstuvwxyz')
    
    while len(word1)>0:
        main_word = " "
        missed=0
        
        for  letter in word1:
            if letter in guessmade:
                main_word+=letter
            else:
                main_word+="_ "
        
        if main_word==word1:
            print(main_word)
            print("you won !!!!")
            break
            
        print("guess the words ",main_word )
        guess=input()
        
        if guess in valid:
            guessmade+=guess
        else:
            print("enter valid character")
            guess=input()
        
        if guess not in word1:
            turns-=1
            
            if turns==9:
                print("9 turns left!!!")
                print("---------------")
            if turns==8:
                print("8 turns left!!!")
                print("----------------")
                print("       O       ")
            if turns==7:
                print("7 turns left!!!")
                print("----------------")
                print("       O       ")
                print("       |      ")
            if turns==6:
                print("6 turns left!!!")
                print("----------------")
                print("       O       ")
                print("       |       ")
                print("      /       ")
            if turns==5:
                print("5 turns left!!!")
                print("----------------")
                print("       O       ")
                print("       |       ")
                print("      / \     ")
            if turns==4:
                print("4 turns left!!!")
                print("----------------")
                print("      \O       ")
                print("       |       ")
                print("      / \     ")
            if turns==3:
                print("3 turns left!!!")
                print("----------------")
                print("      \O/       ")
                print("       |       ")
                print("      / \     ")
            if turns==2:
                print("2 turns left!!!")
                print("----------------")
                print("      \O/ |      ")
                print("       |       ")
                print("      / \     ")
            if turns==1:
                print(" only 1 turns left!!!  hangman on his last breath")
                print("----------------")
                print("      \O/_|      ")
                print("       |       ")
                print("      / \     ")
            if turns==0:
                print("you loose")
                print("you let a good man dai")
                print("----------------")
                print("       O_|      ")
                print("      /|\      ")
                print("      / \     ")  
                break  
                
                
                
name=input("enter your good name -->")
print("Welcome ", name,"!")
print("-------------------------")
print("Try to guess the word in less than 10 attemts-->")
hangman()
