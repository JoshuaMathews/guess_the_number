"""
1. Follow the instructions in the slides to resolve the two issues in the guess the number program.
Note the hints in the issues.
2. Create pull requests, review each other's code.
3. Create a merge conflict, and fix it.
4. Create two new issues requested, assign them, and fix them.
5. Submit a link to your GitHub repository.
"""
import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    """ get user's guess, as an integer number """
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)
    guesses = 0

    while True:
        try: # fix to issue input validation - added ValueError handling
            # guess = int(input('Please enter an integer number: '))
            guess = get_guess()
            guesses = guesses + 1
            result = check_guess(guess, secret)
            print(f'Thank you for entering the number {guess}')
            print(result)

            if result == correct:
                break

        except ValueError:
            print('That was not an integer number. Try again.')

    print(f'Thanks for playing the game! You guessed {guesses} times!')  # fix to issue #42


if __name__ == '__main__':
    main()
