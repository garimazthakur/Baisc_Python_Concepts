# https://github.com/jerry-git/learn-python3
# c
# https://www.kdnuggets.com/2021/11/25-github-repositories-python-developer.html
# https://jerry-git.github.io/learn-python3/notebooks/intermediate/html/idiomatic_misc1.html
# https://stackabuse.com/any-and-all-in-python-with-examples/#any

data = (1,2,3,4)

# list
square_roots_list=[]
for val in data:
    square_root=val**(1/2)
    square_roots_list.append(square_root)
print(square_roots_list)

# using list compehension
square_roots_list_comp=[val**(1/2) for val in data]
print(square_roots_list_comp)
# ************************************************************************************************************************

# set
square_roots_set=set()
for val in data:
    square_root=val**(1/2)
    square_roots_set.add(square_root)
print(square_roots_set)

# using set comprehension
square_root_set_comp={val**(1/2) for val in data}
print(square_root_set_comp)
# **************************************************************************************************************************

# dict
square_roots_dict=dict()
for val in data:
    square_root=val**(1/2)
    square_roots_dict[val]=square_root
print(square_roots_dict)

# using dict comprehensions
square_root_dict_comp={val:val**(1/2) for val in data}
print(square_root_dict_comp)  
# ****************************************************************************************************************************

# dict with a condition
integer_square_roots_dict={}
for val in data:
    square_root=val**(1/2)
    if square_root.is_integer():
        integer_square_roots_dict[val]=square_root
print(integer_square_roots_dict)


# using dict with a comprehension
integer_square_roots_dict={
    val:val**(1/2) for val in data if (val**(1/2)).is_integer()
}
print(integer_square_roots_dict)

# ******************************************************************************************************************************
# Using in for checking presence of an element in a collection
name = "John Doe"
if name in ('John', "Doe", "john Doe"):
    print("This seems to be our guy")


#******************************************************************************************************************************** 
# Chained Comparisions
a,b,c,d=1,2,4,5
if a<b<c<d:
    print('from lowest to highest: a,b,c,d')
#******************************************************************************************************************************** 

# Falsy/Truthy values

my_list= [1,2]
my_dict={}
my_set=set()
my_tuple=tuple()
zero=0

false= False
true= True
my_str=''

my_second_list=['foo']

if not my_list:
    print('Empty list is so empty')
if not my_dict:
    print('Empty dict is also very empty')
if not my_set and not my_tuple:
    print("Same goes for sets and tuples")
if not zero and not false and not None and not my_str:
    print('These are also falsy')
if my_second_list:
    print('This should be true')



#**************************************************************************************************************************************************************************************************

example_collection=[""] 
# first way
any_value_truthy = True
for val in example_collection:
    if val:
        any_value_truthy=True
        break

all_values_truthy=True
for val in example_collection:
    if not val:
        all_values_truthy=False
        break
print(f'any truthy: {any_value_truthy}, all truthy: {all_values_truthy}')

# Second way, more pythonic
# using any and all
# any & all , returns True or False
# The any(iterable) and all(iterable) are built-in
# The method any(iterable) behaves like a series of OR operators between each element of the iterable
# The all(iterable) method evaluates like a series of AND operators between each of the elements in the iterable

#  Note: n Python, the all function returns True if all of the elements of the given iterable are True. The function also returns True when given an iterable of zero length
# https://stackoverflow.com/questions/3275058/reason-for-all-and-any-result-on-empty-lists
#in case of all(), empty list is considered as True too.

any_value_truthy= any(example_collection)
all_values_truthy=all(example_collection)

print(f'any truthy: {any_value_truthy}, all truthy : {all_values_truthy}')
#**************************************************************************************************************************************************************************************************

# Pythonic substitute for ternary operator
# variable = some_condition ? some_value : some_other_value

# first way
some_condition= True
if some_condition:
    variable = 'John'
else:
    variable = 'Doe'
print(variable)

# second way
variable = 'John' if some_condition else 'Doe'
print(variable)

#**************************************************************************************************************************************************************************************************

# Function keywords arguments
def show_person_details(name, is_gangster, is_hacker, age):
    print(f'name:{name}, gangster: {is_gangster}, hacker:{is_hacker}, age:{age}')

show_person_details('John Doe', True, False, 83)  #Positional Arguments

# Better way 
show_person_details('John Doe', is_gangster=True, is_hacker=False, age=83)  #Keyword Arguments
#**************************************************************************************************************************************************************************************************

# Extra: keyword only arguments after `*`
def func_with_loads_of_args(args1, *, arg2=None, arg3=None, arg4=None, arg5='boom'):
    pass
# This won't work because only keyword arguments allowed after *
#func_with_loads_of_args('John Doe', 1, 2)

# This is ok
func_with_loads_of_args('John Doe', arg4='foo',arg5='bar', arg2='foo bar')


# *****************************************************************************************************************************************************************************************************
# Multiple assignment
# original values
a = 1
b = 2

# way1
temp=a
a=b
b=temp
print(a,b)

# more pythonic

c=1
d=2
# swap
c,d= d,c
print(c,d)