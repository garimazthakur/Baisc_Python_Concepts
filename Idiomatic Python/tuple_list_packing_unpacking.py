# https://betterprogramming.pub/unpacking-lists-and-tuples-in-python-9a396578b1df
# (Un)packing
from re import T


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

# Unpacking a range object
a,b=range(2,4)   #for range we need to pass only two values.
print("Unpacking a range object")
print(a)
print(b)



"""
Extended Iterable Unpacking

The issue: While unpacking, we have to mention the number of variables equal to the length of the sequence(list/tuple)

To overcome the issue: Use Extended Iterable unpacking.
                    Extended Iterable unpacking uses the operator *.
                    A variable preceded by the * operator is used for extended unpacking.
                    It will be a list containing all elements from the iterable that is not assigned to variable names.



first, *rest -- It will unpack the first and all the remaining elements to rest.
                rest will be a list of all items except the first element.

first,*middle, last — It will unpack the first element to first and the last element to last. 
                      The remaining elements will be a list of all items except the first and last elements.

*rest, last — It will unpack the last element in last and all the remaining elements to rest. 
                rest will be a list of all items except the last element.

"""


# Extended unpacking (tuples)
 
num=[1,2,3,4,5]
a,b,*c=num
print(a) 
print(b)
print(c)

# Extended unpacking (lists)

num=[1,2,3,5,7,7,8]

a, b, *c= num
print(a)
print(b)
print(c)

# Unpacking first_element vs. rest
num=(1,2,3,4,5)
first, *rest= num
print(first)
print(*rest)

# #unpacking first,middle,last elements

num=(1,2,3,4,5,6,7)
first, *middle, last = num
print(first)
print(*middle)
print(last)

# Unpacking the last element vs. rest
num=(1,2,3,4,5)
*rest,last= num
print(rest)
print(last)


# Ignoring Single Value While Unpacking Tuples/Lists
tt=("red","green","blue")
t1,_,t2= tt
print(t1) #Output:red
print(t2) #Output:blue
print(_)#Output:green

# Ignoring Multiple Values While Unpacking Tuples/Lists
"""
If we need to ignore multiple values while unpacking, we can mention *_

"""
# Ignoring all the values except the first and the last while unpacking 
num=[1,2,3,4,5,6]
t1, *_, t2 = num
print(t1)  #Output: 1
print(t2) #Output: 6

# Unpacking List of Tuples
emp_info= [('name','indhu'),('exp',6),('skill','Python')]
key, value= zip(*emp_info)
print(key)  #Output:('name', 'exp', 'skill')
print(value) #Output:('indhu', 6, 'Python')

def cal(a,b):
    sum = a+b; diff= a-b; mul=a*b; div = a/b;
    return sum, diff, mul, div
result=cal(5,4)
sum, diff,mul,div=result
print ("Addition :", sum) #Output:Addition : 9
print ("Subtraction: ", diff) #Output:Subtraction:  1
print ("Multiplication :", mul) #Output:Multiplication : 20
print ("Division: ",div) #Output:Division:  1.25