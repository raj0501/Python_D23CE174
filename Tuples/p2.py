#Exercise :Level 1

emp_tuple = ()

brother = ('Shyam' ,'Nax' ,'Jimit')
Sister = ('Happy' ,'Shree' ,'Hileri' ,'Hemanshi')

siblings = brother + Sister
print('Siblings' ,siblings)

print('Number of Siblings' ,len(siblings))

father = 'Bhaveshbhai'
mother = 'Bhavishaben'
family_members =  siblings +(father,mother)
print('Family Members' ,family_members)

#Exercise :Level 2


siblings = family_members[:-2]
father,mother =family_members[-2:]
print('Siblings :',siblings)
print('Father :',father)
print('Mother :',mother)

fruits =('Banana' , 'Apple' ,'Orange')
vegetables =('Chili','Tomato','Potato','Brinjal')
animal =('Cow','Lion','Tiger')
food_stuff_tp =fruits + vegetables + animal
print('FOOD_STUFF_TF :',food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print('FOOD_STUFF_LT :' ,food_stuff_lt)
middle =int(len(food_stuff_tp)/2)
print('Middle :',food_stuff_lt[middle:])

print('First Three :' ,food_stuff_lt[0:3])
print('Last Three :' ,food_stuff_lt[-3:])

del food_stuff_tp

nordic_countries = ('Denmark','Finland','Iceland','Norway','Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

