# Translate words into Giraffe Language.
# All vowels replaced with the letter G.

def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

print(translate('Good Morning')) 