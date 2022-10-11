# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line
letter_grades = 'ABCDF'
print(letter_grades[-1])
print(letter_grades[-2])
print(letter_grades[-2] == letter_grades[3])

waltz = 'onetwothree'
waltz[0:3]
# We don't need to specify the 0 if we start at the beginning
waltz[:3]
waltz[3:6]
waltz[6:11]
# Same goes for the end -- we can leave it empty
waltz[6:]
# We can specify a step size if we don't want a continuous slice
print(waltz[0:11:2])