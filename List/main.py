even=[2,4,6,8]
odd=[1,3,5,7,9]

# *****************************************Zip and UnZip*****************************************************************
"""
Ziping and Unziping of list 
"""
# Zipping two lists
Zip_list= list(zip(even, odd))
# print(Zip_list)  #output: [(2, 1), (4, 3), (6, 5), (8, 7)]

# Unzipping tow lists
even , odd = zip(*Zip_list)
# print(even)  #output: (2, 4, 6, 8)
# print(odd)  #output: (1, 3, 5, 7)




# *****************************************Concatination*****************************************************************
"""
Concatenation lists using
"""
even1=[2,4,6,8]
odd1=[1,3,5,7]
# Using append
 
# method 1  *********append*******
lis = [even1, odd1]
nums= []
print(lis) #output: [[2, 4, 6, 8], [1, 3, 5, 7]]
for y in lis:
    for l in y:
        # x = [l]
        nums.append(l)
print(nums)

# method 2 *********append*******
lis = [even1, odd1]
for num in odd1:
    even1.append(num)
print(even1)
print("****************************************+++++++++++++++")

# ********Using list comprehensions**********
lis = [even1, odd1]
lis_concat= [y for x in lis for y in x]
print(lis_concat)


# ********Using extend**********
# Using extend
even=[2,4,6,8]
odd=[1,3,5,7,9]
even.extend(odd)
print(even)


# ********Using  + operator**********
#Using operator
output=even + odd
print(output)

# ********Using  + operator**********
output= [*even, *odd]
print(output)

# *********Using itertools.chain()*********
# https://docs.python.org/3/library/itertools.html
import itertools
print(list(itertools.chain(even, odd)))




