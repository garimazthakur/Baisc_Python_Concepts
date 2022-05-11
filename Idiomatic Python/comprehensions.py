# https://jerry-git.github.io/learn-python3/notebooks/beginner/html/strings.html

# https://www.kdnuggets.com/2021/11/25-github-repositories-python-developer.html

# https://jerry-git.github.io/learn-python3/notebooks/beginner/html/strings.html
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

my_list= []
my_dict={}
my_set=set()
my_tuple=tuple()
zero=0
false= False
true= True
my_str=''



