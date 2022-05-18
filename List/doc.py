
#lists are a mutable type
squares = [1, 4, 9, 16, 25]
print(squares)
# indexing returns the item

print(squares[0])   #output: 1
print(squares[-1])   #output: 25
print(squares[-3:])   #output: [9,16,25]
print(squares[:])   #output: [1, 4, 9, 16, 25]
print(squares + [36, 49, 64, 81, 100]) #output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

cubes = [1, 8, 27, 65, 125]
cubes[3]=64
print(cubes)  #[1,8,27,64,125]

cubes.append(216)   #add cube of 6
cubes.append(7**3)  #add cube of 7
print(cubes)  #output: [1, 8, 27, 64, 125, 216, 343]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters) #['a', 'b', 'C', 'D', 'E', 'f', 'g']

letters[:] = []
print(letters)  #output: []
print(len(letters))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a,n]
print(x) #output: [['a', 'b', 'c'],[1, 2, 3]]

y= x[0][1]
print(y)