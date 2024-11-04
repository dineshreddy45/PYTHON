import random
def NUMBER_GAME():
    random_number=random.randint(1,100)
    print("The random integer is:-", random_number)
    for i in range(3):
        guess_number=int(input( "Please enter the number that you want to guess:-  "))
        if  random_number == guess_number :
            print("You guessed the number corret hurray")
            break
        else:
            if abs(guess_number -  random_number) <= 10:
                print("Number is close thing again")
            else:
                    print( "The number is far away")

    user_input=input("Do you want to play again:-Yes/No ")

    if user_input == "Yes":
        NUMBER_GAME()
    else:
        print("Thank you for playing")
test=NUMBER_GAME()