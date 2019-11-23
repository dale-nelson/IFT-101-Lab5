progWords = {}

progWords['elements'] = '''
Each array memory location is called an element and is given a number or numbers
corresponding to the position of the location in the array.
'''
progWords['stack'] = '''
A stack is a list of numbers, such as an array of numbers, to which all additions 
are at one end and all deletions are at the same end.
'''
progWords['queue'] = '''
A queue is a list that adds data to one end and deletes data from the other end
'''
progWords['pointer'] = '''
Pointing the value of the element in the first array to the element in the second
'''
progWords['accumulating'] = '''
Summing a group of numbers using variables instead of constants
'''

for key, value in progWords.items():
    print(key.title() + ":")
    print(value.lstrip())