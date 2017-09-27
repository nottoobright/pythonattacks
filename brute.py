import itertools
import string

pass_length = int(input("Enter length: "))
password = input("Enter password: ")

def guess_password(password):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(1, pass_length):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)

print(guess_password(password))
