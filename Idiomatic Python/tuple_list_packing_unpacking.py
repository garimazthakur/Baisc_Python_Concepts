# https://betterprogramming.pub/unpacking-lists-and-tuples-in-python-9a396578b1df
# (Un)packing
print("*******************************************Tuple*******************************************************************************")

"""
Packing, Unpacking Python Tuples

Packing - Assigning multiple values to one tuple
Unpacking - Multiple assignment, assigning values from tuple to many variables.\

Unpacking can be done on sequences (lists, tuples, ranges)
 
"""
# Tuple Packing
emp_info='Python',5,'Developer'
print(emp_info)
# output('Python', 5, 'Developer')

# Tuple Unpacking
skill, exp, role= emp_info
print(skill)  #output: Python
print(exp)    #output: 5
print(role)   #output: Developer

print("**************************************************List************************************************************************")

"""
We can unpack two Python lists into a single variable.
It will return a tuple containing all the elements from both lists.

"""
# Unpacking Python List, Range Object
even = [2,4,6]
odd=[1,3,5]
num= *even , *odd 
print(num)  #output: (2, 4, 6, 1, 3, 5)

# Unpacking two Python lists to a single list
even=[2,4,6,8]
odd=[1,3,5,7,9]
num= *even , *odd 
print(list(num)) #output: [2, 4, 6, 8, 1, 3, 5, 7, 9]

num1 = even +odd 
print(num1)













print("*************************************")
my_list=[1,2,3,4,6,7,8,0]
first = my_list[0]
last=my_list[-1]
middle=my_list[1:-1]
# print(first, middle, last)
# packing 
packed=[first]+middle+[last]   #middle already in list
print(packed)
assert packed==my_list


# *****************************************************************************************************************************************************************************************************
# *****************************************************************************************************************************************************************************************************
# *****************************************************************************************************************************************************************************************************
# *****************************************************************************************************************************************************************************************************

#  unpacking
my_list=[5,6,7,89,0]
first, *middle, last= my_list
# print(first, middle, last)
packed=[first, *middle, last]
print(packed)
assert packed==my_list






