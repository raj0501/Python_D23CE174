# D23CE174 Raj Makwana


# A) Create a list and apply methods (append, extend, remove, reverse), arrange created list in ascending and descending order.


a=[10,20,30,40,50]
print('List : ',a)
a.append(60)
print('Append 60 : ',a)
a.extend([80,90,174])
print('Extend List with [80,90,174] : ',a)
a.remove(20)
print('Remove : ',a)
a.reverse()
print('Reverse List : ',a)
a.sort()
print('Sorted List : ',a)
a.sort(reverse=True)
print('Decending List : ',a)


# B) List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", "orange"]] From above list get word “orange” and “Python” & repeat this list five times without using loops


list = [1, 2, 3, 4, ["python","java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana","orange"]]
print(list)
word_python = list[4][0]
print('Word 1 : ',word_python)
word_orange = list[8][2]
print('Word 2 : ',word_orange)
print(list*5)

# C) Create a list and copy it using slice function

list = [1, 2, 3, 4, 5,6,7,8,9,10]
print("Original List:", list)
copied_list = list[:]

print('Slice Opration With Range: ',list[slice(2,5)])
print('Slice Opration With Jump : ',list[slice(1,9,2)])
print('Slice Opration With Ending : ',list[slice(7)])
print("Copied List:", copied_list)

#D) Create a tuple and apply different type of mathematical operation on it (Sum, Maximum, minimum etc.).

tupple1 = (10,20,30)
tupple2 = (40,50,60)
print("Printing 1st Tupple : ", tupple1)
print("Printing 2st Tupple : ", tupple2)
print("Printing Addition of Tupple : ", tupple1 + tupple2)
print("Printing Minimum of Tupple1: ", min(tupple1 + tupple2))
print("Printing Maximum of Tupple1: ", max(tupple1 + tupple2))


