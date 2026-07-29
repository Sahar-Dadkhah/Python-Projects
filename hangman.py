import random
from hangmantools import logo, stages, word_list
print(logo)
chosen_word=random.choice(word_list)
lives=6
print(f"Pssst, the solution is {chosen_word}")
end_of_game=False
display=[]
for letter in chosen_word:
    display+="_"

while not end_of_game:
    guess=input("Guess a letter : ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose!")



    print(display)
    if "_" not in display:
        end_of_game=True
        print("You win!")
    print(stages[lives])
input("")


