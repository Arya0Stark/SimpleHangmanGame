import random


movie_list= ["Sinister", "Hangover","Avatar","Insidious", "Chuckie","Godfather","Terminator","Tangled","Mulan"]

print("\n this is a guessing game, more or less like hangman.\n",
      "you will be given a movie name(English) with vowels only.\n",
      "your guess limit is 10, and your guess input should be 1 consonant only")
n= random.choice(movie_list)
def guess(n):
    x= n.upper()
    guess_count=0
    guess_limit=10
    
    a=""
    for i in x:
        if i not in 'AEIOU':
            a= a + "_"
        
        else:
            a= a + i
    
    print(a)
    
    lis=[]
    while guess_count!=guess_limit:
        
        l=input("Enter a letter to guess the movie further :):\n")
        new_a=""
        lis.append(l.upper())
        for let in x:
            if let in 'AEIOU':
                new_a+=let
            elif let in lis:
                new_a+=let
            else:
                new_a= new_a+"_"
        print(new_a)  
        
        
        
        guess_count+=1
            
        print("You have ",guess_limit-guess_count, "guesses lef.t")
        if new_a==x:
            print("Congrtaulations! You guessed right! :(")
            break
        if guess_count==guess_limit:
            print("Oops! Looks like you're clean out of guesses :(")
        y="Hope you enjoyed playing!"

    return y
        
print(guess(n))



        
        
    
    




















