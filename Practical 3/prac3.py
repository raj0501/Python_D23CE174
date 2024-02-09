# D23CE174 Raj Makwana

# A) String Operations:
# Reverse a string, replace string with other string, merge two strings

s = str(input("Enter String : "))
rs = s[::-1]
print("String : ",rs)
replaces = str(input("Enter String to be replaced: "))
s2 = s.replace(s, replaces)
print("Replaced String : ",s2)
print ("Merged String is : ", s+ " " +s2)

# Find character is in string or not without using loops

string = str(input("Enter String : "))
findc = str(input("Enter character : "))
index = string.find(findc)  
  
if index != -1:  
    print("The character "+ findc + " is present in the string at: ", index+1)  
else:  
    print('The character is not present in the string')  
            
# Split string into multiple words &characters
     
string = "Hello World!"
words = string.split()
print(words)

characters = list(string)
print(characters)



# B) Dictionaries Operations:


#  Apply “Update, Delete, clear, popitem, pop, get, keys and values” operation in dictionary.

raj_dict = {'name': 'Raj', 'age': 18}
raj_dict.update({'city': 'Keshod', 'age': 20})
print("Updated dictionary:",raj_dict)  
del raj_dict['age']
print("Dictionary after deleting 'age':", raj_dict)
raj_dict.clear()
print("Dictionary after clearing:", raj_dict)

dict1 = {'a': 174, 'b': 2,'c': 3, 'd': 4}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}
merged_dict = dict1 | dict2 | dict3
print("Merged dictionary:", merged_dict)
popped_item = dict1.popitem()  
print("Popped item:", popped_item)
print("After Popped dictionary:", dict1)
popped_value = dict1.pop('c') 
print("Popped value:", popped_value)
print("After Popped dictionary:", dict1)
name = dict1.get('name', 'Not found')  
print("Name:", name)
keys = dict1.keys() 
print("Keys:", keys)
values = dict1.values() 
print("Values:", values)
dict1 = {'a': 174, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}
merged_dict = dict1 | dict2 | dict3
print("Merged dictionary:", merged_dict)

# Create 3 dictionaries and merge them into 1 dictionary

dict1 = {'a': 174, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

merged_dict = dict1 | dict2 | dict3
print("Merged dictionary:", merged_dict)
