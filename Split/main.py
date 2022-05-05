email = " garima@thakur6@gmail@com "
print(email.split("@",1))    
print(email.split("@",2))
print(email.split("@",5))
print(email.rsplit("@",1))
print(email.rsplit("@",2))
print(email.strip().split("@",1))
print(email.strip().rsplit("@",1))

# Output:
# [' garima', 'thakur6@gmail@com ']
# [' garima', 'thakur6', 'gmail@com ']
# [' garima', 'thakur6', 'gmail', 'com ']
# [' garima@thakur6@gmail', 'com ']
# [' garima@thakur6', 'gmail', 'com ']
# ['garima', 'thakur6@gmail@com']
# ['garima@thakur6@gmail', 'com']

email1 = " garima.thakur6@gmail.com "
print(email1.split("@",1))  #split(separator, max_num_of_splits) method splits a string into an array of substrings. 
print(email1.rsplit("@",1)) # The rsplit(separator, max_num_of_splits) method splits a string into a list, starting from the right.
print(email1.strip().split("@",1))
print(email1.strip().rsplit("@",1)) 

# output:
# [' garima.thakur6', 'gmail.com ']
# [' garima.thakur6', 'gmail.com ']
# ['garima.thakur6', 'gmail.com']
# ['garima.thakur6', 'gmail.com']