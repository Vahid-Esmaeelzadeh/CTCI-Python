'''
Dictionary sorting
'''

my_dict = {10: 'Google',
            7: 'Amazon',
            5: 'Facebook',
            8: 'LinkedIn'}

my_dict1 = {10: ['Google', 330],
            7:  ['Amazon', 320],
            5:  ['Facebook', 280],
            8:  ['LinkedIn', 300]}

# original dictionary
print(my_dict)

# sorted keys
print(sorted(my_dict))

# using for loop iterating over keys
for key in sorted(my_dict):
    print((key, my_dict[key]))

# using dict.items() and lambda
print(sorted(my_dict1.items(), key=lambda kv: (kv[0], kv[1])))
# sort based on values
print(sorted(my_dict1.items(), key=lambda kv: (kv[1][1], kv[0]), reverse=True))

print(sorted(my_dict1.values(), key=lambda v: (v[1], v[0]), reverse=True))



