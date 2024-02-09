# Practical Task
# D23CE174 Raj Makwana
# 1
def reverse_string(input_string):
    return input_string[::-1]

org_str = "D23CE174"
reversed_str = reverse_string(org_str)

print("Org String:", org_str)
print("Reversed String:", reversed_str)

# 2

org_str = "D23CE174"
modified_str = org_str.replace('D', 'd')

print("Org String:", org_str)
print("Modified String:", modified_str)

# 3

input_str = "D23CE174"
find = 'D'

if find in input_str:
    print(f"The character '{find}' found")
else:
    print(f"The character '{find}' not found")

# 4
    

raj_tuple = (1, 2, 3, 4, 174)
raj_list = [10, 20, 30, 40, 174]
raj_set = {11, 22, 33, 44, 174}

tuple_as_string = str(raj_tuple)
list_as_string = str(raj_list)
set_as_string = str(raj_set)

print("Tuple as string:", tuple_as_string)
print("List as string:", list_as_string)
print("Set as string:", set_as_string)


# 5

input_str = "D23, CE174"
upper_case_str = input_str.upper()
lower_case_str = input_str.lower()
split_whitespace = input_str.split()
split_comma = input_str.split(',')

print("Org String:", input_str)
print("Upper Case String:", upper_case_str)
print("Lower Case String:", lower_case_str)
print("Split with Whitespace:", split_whitespace)
print("Split with Comma:", split_comma)

# 6


raj_tuple = (5, 10, 3, 8, 174)
raj_list = [7, 2, 11, 6, 174]

max_tuple = max(raj_tuple)
max_list = max(raj_list)
min_tuple = min(raj_tuple)
min_list = min(raj_list)
length_tuple = len(raj_tuple)
length_list = len(raj_list)
sum_tuple = sum(raj_tuple)
sum_list = sum(raj_list)


print("D23CE174 Tuple:", raj_tuple)
print("D23CE174 List:", raj_list)
print("Maximum in Tuple:", max_tuple)
print("Maximum in List:", max_list)
print("Minimum in Tuple:", min_tuple)
print("Minimum in List:", min_list)
print("Length of Tuple:", length_tuple)
print("Length of List:", length_list)
print("Sum of Tuple:", sum_tuple)
print("Sum of List:", sum_list)

# 7


org_list = [1, 2, 3, 4, 174]
copied_list = org_list[:]

print("org List:", org_list)
print("Copied List:", copied_list)

# 8

#8.1
student = {
    'name': 'Raj Makwana',
    'age': 19,
    'grade': 'A'
}

name_value = student['name']
age_value = student['age']
grade_value = student['grade']

print("Name:", name_value)
print("Age:", age_value)
print("Grade:", grade_value)

#8.2

print("Org Age:", student['age'])

new_age = 21
student['age'] = new_age
print("Modified Age:", student['age'])


#8.3

print("Org Grade:", student['grade'])

new_grade = 'B'
student['grade'] = new_grade
print("Updated Grade:", student['grade'])

#8.4

if 'gender' in student:
    print(" gender is in dictionary.")
else:
    print(" gender is not in dictionary.")

#9

#9.1

set1 = {174, 2, 3}
set2 = {3, 4, 5}

print("Set 1:", set1)
print("Set 2:", set2)

union_set = set1.union(set2)
print("Union of Sets:", union_set)

#9.2

intersection_set = set1.intersection(set2)
print("Intersection of Sets:", intersection_set)

#9.3

difference_set = set1.difference(set2)
print("Elements in Set1 but not in Set2:", difference_set)

#9.4

is_subset = set1.issubset(set2)
if is_subset:
    print("Set 1 is a subset of Set 2.")
else:
    print("Set 1 is not a subset of Set 2.")

#10

#10.1
    
subjects_dict = {
    'math': {'Raj', 'Daksh', 'Samarth'},
    'science': {'Raj', 'Jimit', 'Utsav'}
}
print("Subjects Dict:", subjects_dict)

new_student = 'Prit'
subjects_dict['math'].add(new_student)
print("Updated Subjects Dict:", subjects_dict)

#10.2

student_remove = 'Jimit'
subjects_dict['science'].remove(student_remove)
print("Updated Subjects Dict:", subjects_dict)

#10.3

common_students = subjects_dict['math'].intersection(subjects_dict['science'])
print("Students who take both 'math' and 'science':", common_students)

#10.4

world_population = {
    'India': {'Ahemdabad': 111111, 'Mumbai': 222222 , 'Bangalore': 333333},
    'China': {'xyz': 174174, 'raj': 174174, 'makwana': 174174},
    'USA': {'New York': 444444, 'raj': 5555555, 'Chicago': 6666666}
}
print("World Population Dictionary:", world_population)

#11


org_list = [174 , 1, 2, 3, 4, 5, 6, 7, 8, 9]

even_indices_list = org_list[::2]
odd_indices_list = org_list[1::2]

print("Original List:", org_list)
print("List at Even Indices:", even_indices_list)
print("List at Odd Indices:", odd_indices_list)

#12

a=10
b=20
a,b=b,a
print("Swapped values a:", a)
print("Swapped values b:", b)

# 13

def is_palindrome(input_list):
    return input_list == input_list[::-1]


raj_list = [174, 23, 1 , 23, 174]

if is_palindrome(raj_list):
    print("Palindrome.")
else:
    print("Not palindrome.")

# 14

tuple1 = (174, 2, 3)
tuple2 = (4, 5, 6)

concatenated_tuple = tuple((*tuple1, *tuple2))
print("Concatenated Tuple:", concatenated_tuple)
