import random


# Task 1: Guess the number through user input
def guess_random_number(tries, start, stop):
    # Use the random module to generate a random number between the start and stop integers, inclusive.
    target = random.randint(start, stop+1)

    # Write a while loop that loops as long as tries is not equal to 0.
    while tries != 0:   # Inside the while loop, print the number of tries remaining.
        print("Number of tries left:", tries)

        # Prompt the user to input a guess.
        guess = int(input("Guess a number between 0 and 10: "))

        # Compare the number guessed to the target number (the random number you previously created).
        # If they are equal, print a success message and return out of the function.
        if str(guess) == str(target):
            print("You guessed the correct number!")
            return target
        # If the number guessed is less than the target number, print "Guess higher!"
        elif str(guess) < str(target):
            print("Guess higher!")
        # If the number guessed is greater than the target number, print "Guess lower!"
        elif str(guess) > str(target):
            print("Guess lower!")

        tries -= 1   # Decrement the value of tries by 1.

        # If the user does not successfully guess the number by the time that tries has reached the number 0 and the while loop exits, then print a failure message.

        if tries == 0:
            print("You have failed to guess the number:" + str(target))


'''
Call the guess_random_number() function.
Provide arguments such that the value of tries in the function will be initialized to 5, and the random number will be 
generated in the range of 0 to 10 inclusive. 
'''
guess_random_number(5, 0, 10)


# Task 2: Guess the number programmatically through linear search
def guess_random_num_linear(tries, start, stop):
    # se the random module to generate a random number between the start  and stop integers, inclusive.
    target = random.randint(start, stop+1)

    print("The number for the program to guess is: " + str(target))

    # For loop to implement the linear search algorithm to compare each integer in the potential range to the randomly generated target number.
    for x in range(0, 10):

        guess = 0

        while tries != 0:
            print("Number of tries left:", tries)
            print("The program is guessing... " + str(guess))

            # Every time the computer makes a comparison, that is one guess. Decrement the tries variable and stop the function (using return) when there are no more tries left.
            guess += 1

            tries -= 1

            # Show the target number, show each guess that the computer makes, and show appropriate success/failure messages.
            if guess == target:
                print("The program has guessed the correct number!")
                return x
            else:
                print("The program has failed to guess the correct number.")

    return -1


# Since there are 11 potential numbers, and the computer only gets 5 tries, the computer will guess correctly around half the time, and incorrectly the other ~half.
'''guess_random_num_linear(5, 0, 10)'''


# Task 3: Guess the number programmatically using binary search.
def guess_random_num_binary(tries, start, stop):
    # se the random module to generate a random number between the start and stop integers, inclusive.
    target = random.randint(start, stop)

    print("Random number to find: " + str(target))

    # Lower and upper bounds set to start and stop arguments
    lower_bound = start
    upper_bound = stop

    '''
    Set a pivot_value, which is at the halfway point between the lower and upper bounds. The floor division operator (//) ensures that we get a rounded-down 
    integer value as the pivot index. We then retrieve the value at the pivot index from the list.
    '''
    while tries:
        pivot = (lower_bound + upper_bound) // 2

        # If statement to see if pivot is greater, less than , or equal to the target.
        if pivot == target:
            print("Found it! " + str(target))
            return pivot
        elif pivot < target:
            print("Gussing higher!")
            # discard the lower half of the list by setting the upper bound to the index just below the pivot
            lower_bound = pivot + 1
        elif pivot > target:
            print("Guessing lower!")
            # discard the upper half of the list by setting the upper bound to the index just below the pivot.
            upper_bound = pivot - 1
        tries -= 1

    print("Your program failed to find the number")

    '''
    If the while loop exits without returning from the function, that means the target value was not found in the list, and we can return -1 as the result to 
    indicate that this has happened.
    '''
    return -1


'''guess_random_num_binary(5, 0, 100)'''


'''
Bonus Task 1
Add validation in guess_random_num() such that a user can only enter integers within the given range. 

Bonus Task 2
Write a function that, when called, will ask the user to input the number of tries, and the range (start and stop values). 
Then have the user choose whether to guess a random number using user input, linear search, or binary search.
Then run the chosen variation with the provided arguments.

Bonus Task 3
Add code in the guess_random_num() function such that the user is not permitted to enter the same guess more than once. 
Hint: You can use a data structure to store guesses, then compare new guesses against the stored guesses.

Bonus Task 4
Write a function that acts as a gambling game:
When called, it should ask the player to bet on whether the computer will or will not guess the correct number. 
The player starts out with $10 and can bet $1 to $10 max, in integer increments of $1. The player cannot bet more $ than they have. 
The program should call the guess_random_num_linear() function with arguments that would produce a 50/50 chance, or near it.
If the player bet correctly, the player doubles their bet. If the player bet incorrectly, the player loses their bet.
If the player runs out of money, the player loses and the game is over.
If the player reaches > $50, the player wins and the game is over.
'''
