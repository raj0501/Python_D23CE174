dog = {}

dog = {
    'name' :'Roki',
    'color':'black',
    'breed':'Doberman',
    'legs':4,
    'age':2
}
student ={
    'first_name' : 'Raj',
    'Last_name' : 'Makwana',
    'Gender' :'male',
    'age' : 19,
    'maritial_status':'unmarried',
    'skills':['Java','.Net','javascript','dsa'],
    'country':'India',
    'city':'Keshod',
    'address' :'Somewhere in keshod'
}

print('Length :' ,len(student))

print('Skills :',student.get('skills'))

student['skills'].append('React')
student['skills'].append('Mongodb')
print('Skills :',student.get('skills'))

print('Keys :',student.keys())

print('Values :',student.values())

list =list(student.items())
print('List :' ,list)

student.pop('maritial_status')
print('Student :' ,student)

del dog