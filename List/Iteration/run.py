list1= [(2,3), (4,5), (6,7)]

k, v  = zip(*list1)
print(k)  #(2, 4, 6)
print(v) #(3, 5, 7)
# ********************************
print(list1[1][0])  #4
for x in list1:
    print(x[0]) 
    #output: 
    # 1
    # 2
    # 3  
    
for inde, val in enumerate(list1):
    print(val)
    # output
    # (2, 3)
    # (4, 5)
    # (6, 7)


print("*********************************************")

list2= [5, 2,3, 4,5, 6,7]
lis= []
lis1=[]
lis2=[]
for idx, value in enumerate(list2):
    
    pair = idx, value
    lis.append(pair)
    
    _, pair1= idx, value
    lis1.append(pair1)
    
    pair2, _ = idx, value 
    lis2.append(pair2)

print(lis) # [(0, 5), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
print(lis1) #[5, 2, 3, 4, 5, 6, 7]
print(lis2) #[0, 1, 2, 3, 4, 5, 6]

   
    
    