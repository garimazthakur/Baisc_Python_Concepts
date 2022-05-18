# https://jerry-git.github.io/learn-python3/notebooks/intermediate/html/idiomatic_misc2.html
#string concatinaton

names= ('John', 'Lisa', 'Terminator', 'Python')
#using a loop
semicoln_seperated = names[0]
print(semicoln_seperated)
for name in names[1:]:
    semicoln_seperated+= ';'+ str(name)
print(semicoln_seperated) #output: John;Lisa;Terminator;Python

print("*****************************************")

#using join method
semicolon_seperated= ";".join(names)
print(semicolon_seperated)   #output: John;Lisa;Terminator;Python

"""
    or in assignments
    
    The return value of a or b:
    a is truthy
    b otherwise
    
"""
a=0
b=None
c ='John Doe' 
my_variable='default value'
if a: 
    my_variable=a 
elif b:
    my_variable =b
elif c:
    my_variable=c
print(my_variable)  #output John Doe

#in one line
my_variable= a or b or c or 'defauly value'
print(my_variable) #output John Doe



#try - except - else
try:
    cal= 1/0   #ogic
    
except ValueError as e:
    print(f'this is wrong, some keyerror: {e}')
except Exception as e:
     print(f'this is wrong, somthing bad happened: {e}')
else:
    print('All is well')    
    
#try-finally
def cal():
    try:
        cal= 1/0  #logic
    except ZeroDivisionError:
        return 0
    except Exception:
        return None
    finally:
        print("This is cool")
    return cal

print(f'return value : {cal()}')


#
        
    
    
    



