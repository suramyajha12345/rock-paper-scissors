import random 

print ("Welcome to the rock,paper,scissors game!")

random_number = random.randint(1,3)
dict_num = {1: "rock", 2: "scissors", 3: "paper"}

user_input = input("Enter a anythong among rock,paper and scissors: ").lower()

if user_input not in dict_num.values() :
    print ("Please enter something only among rock,paper and scissors")

computer_choice = dict_num[random_number]
print (f'Computer chose: {computer_choice}')

if computer_choice == user_input:
    print ("It's a tie ")
elif computer_choice == "paper" and user_input == "rock":
    print ("You lose!")
elif computer_choice == "scissors" and user_input == "paper":
    print ("You lose!")
elif computer_choice == "rock" and user_input == "scissors":
    print ("You lose!")
else:
    print ("You win!")