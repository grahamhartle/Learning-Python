# A guessing game

secret_word = 'giraffe'
guess = ''
points = 100

print('What animal am I thinking about?')

while guess != secret_word:
    guess = input('Enter your guess: ')
    if guess != secret_word:
        points -= 10

print('Weldone! You guessed correctly.')
print(f'You scored {points} points')