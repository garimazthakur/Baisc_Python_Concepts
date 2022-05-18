
#if there is spacy between the strings, they are automtically connected
# This only works with two literals though, not with variables or expressions
# Python strings cannot be changed — they are immutable
x= "py" "thon"   
print(x) #output: python

y = "Garima" "ai"
print(y) #output: Garimaai

z= ("Put several strings with parentheses " 
"to have the joined together")
print(z)  #output: Put several strings with parentheses to have the joined together


prefix = 'Py'
# prefix 'thon'  # can't concatenate a variable and a string literal
# output: SyntaxError: invalid syntax

# If you want to concatenate variables or a variable and a literal, use +
v= prefix + 'thon'  #now it will work  
print(v) #output: python

word = "python"
print(word[0])    #output: p
print(word[5])    #output: n
print(word[-1])   #output: n
print(word[-2])   #output: o
print(word[-6])   #output: p
print(word[0:2])      #output: "py"
print(word[2:5])      #output: "tho"
print(word[:2])      #output: "py"
print(word[4:])      #output: "on"
print(word[-2:])      #output: "on"

print(word[:2] + word[2:])  #output: "python"
print(word[:4] + word[4:])  #output: "python"
print(word[4:42])  #output: "py"
print(word[42:])  #output: ""

# Python strings cannot be changed — they are immutable.
# But if you need to change this:
# word[0] = 'J'
# print(word)  #output: error: TypeError: 'str' object does not support item assignment

z= 'J' +word[1:]
print(z) #output: Jython
word[2:]+'py'
print(word[2:]+'py')  #output: thonpy

s = 'supercalifragilisticexpialidocious'
print(len(s))



