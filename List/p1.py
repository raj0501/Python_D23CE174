# Exercises : Level 1


e_l = list()
print('Empty List Lenght',len(e_l))


subject  = ['PYTHON','SE','DAA','DBMS','DCN','SGP','HS']
print('My List : ',subject)


print('length :',len(subject))

first=subject[0]
middle=subject[int((len(subject)-1)/2)]
last=subject[len(subject)-1]


print('First Item :',first)
print('Middle Item :',middle)
print('Last Item :',last)

mix_data_types = ['Raj Makwana',19,5.5,'unmarried','Changa']
print('Mix_Data_Types :',mix_data_types)

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print('It_companies : ',it_companies)

print('Number of Companies :',len(it_companies))

first=it_companies[0] 
middle=it_companies[int((len(it_companies)-1)/2)]
last=it_companies[len(it_companies)-1]

print('First company :',first)
print('Middle company :',middle)
print('Last company :',last)

it_companies[4]='TCS'
print('After Modify :',it_companies)

it_companies.append('IBM')
print('After Adding one Company :',it_companies)

it_companies.insert(int((len(it_companies)-1)/2),'Ttf')
print('After Adding At middle :',it_companies)

it_companies[0]=it_companies[0].upper()
print('After uppercase :',it_companies[0])

join_it = '#;&nbsp '.join(it_companies)
print('Aftre Jointing  :' , join_it)

print('Cheack Apple Compnay in list or not :' ,"Apple" in it_companies)

it_companies.sort()
print('After Sorting using sort :',it_companies)

it_companies.reverse()
print('After Reverse using reverse :',it_companies)

print('Slice out the first 3 companies :',it_companies[0:3])

print('Slice out the last 3 companies :',it_companies[-3:])

slice_middle = it_companies[int((len(it_companies)-1)/2)]
print('slice Middle :',slice_middle)

del it_companies[0]
print('After delete 1st it company :',it_companies)

remove_middle = int((len(it_companies)-1)/2)
it_companies.pop(remove_middle)
print('After delete middle :',it_companies)

it_companies.pop()
print('Aftre delete last :',it_companies)

it_companies.clear()
print('After remove all :',it_companies)

del it_companies
print('Detroy successfully')

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
f_b_join = front_end + back_end
print('After Join :',f_b_join)

full_stack = f_b_join
full_stack.insert(5,'Python') 
full_stack.insert(6,'SQL')
print('After Copy and append :',full_stack)

# Exercises : Level 2

student_ages = [19,22,19,24,20,25,26,24,25,24]

student_ages.sort()
print('Student Ages :',student_ages)
min_age =min(student_ages)
max_age =max(student_ages)
print('Minimum Studnet age :',min_age)
print('Maximum Studnet age :',max_age)

student_ages.append(min_age)
student_ages.append(max_age)
print('Append :' ,student_ages)

mid=int(len(student_ages)/2)
print('Mid Age :',student_ages[mid]/2)

avg =sum(student_ages)/len(student_ages)
print('Avg of ages :',avg)

range =max(student_ages) -min(student_ages)
print('Range :',range)

min_avg = min_age -avg
max_avg = max_age-avg
print('abs min_avg :',abs(min_avg))
print('abs max_avg :',abs(max_avg))

countries =['China','Russia','USA','Finland','Sweden','Norway','Denmark']
mid_country =int(len(countries)/2)
print(countries[mid_country])

f_part = (countries[:mid_country])
s_part = (countries[mid_country:])
print('First Part :',f_part)
print('Second Part :',s_part)

scandic_countries = s_part
print('Scandic countries :',scandic_countries)