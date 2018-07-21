# A guessing game

secret_word = 'giraffe'
guess = ''
points = 100

print('What animal am I thinking about?')

while guess != secret_word and points >0:
    guess = input('Enter your guess: ')
    if guess != secret_word:
        points -= 10

if points == 0:
    print('You have not guessed correctly.')
else:
    print('Weldone! You guessed correctly.')
    print(f'You scored {points} points')