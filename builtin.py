import random as rd
 
numberList = [111,222,333,444,555]
print("random item from list is: ", rd.choice(numberList))


import array
myarryobj = array.array('l', [1,2,3,4])
type(myarryobj)
id(myarryobj)
myarryobj.extend([6])
id(myarryobj)
print(myarryobj)
