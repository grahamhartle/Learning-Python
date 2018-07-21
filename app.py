# getting input from a user
name = input('Enter your name: ')
print(f'Hello {name} how are you?')
response = input('I\'m feeling ')
if response == 'ok':
  print('Glad to hear it')
elif response == 'good':
  print('I\'m feeling good too')
else:
  print('Sorry to hear that!')
