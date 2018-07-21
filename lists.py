# lists
friends = ['John', 'Joe', 'Fred', 'Ann', 'Mick']

# # list index starts at [0]
# print(friends[0])

# # print list from index [2]
# print(friends[2:])

# # print list from [0] - [2]
# print(friends[0:3])
# # prints the list from the first index
# # to the third index, but it does not include the third index value

# # print from the last index position
# print(friends[-1])

# # append new item to the end of the list
# friends.append('Bert')
# print(friends)

# # insert new item into the list - parameters are index position and name
# friends.insert(2, 'Mary')
# print(friends)

# # remove item from the list
# friends.remove('Fred')
# print(friends)

# pop removes the last item from the list
# saved_name = friends.pop()
# print(friends)
# print(saved_name)

# sort a list
# friends.sort()
# print(friends)

# reverse the list
friends.reverse()
print(friends)