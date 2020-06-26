lam = lambda a : a * 2
print(lam(22))
f = lambda x, y : x + y
print(f(2,2))
lam1 = lambda a: "Even" if a%2==0 else "Odd"
print(lam1(101))

list1 = [1,2,3,4,5,6,7,8,9,10]
evenList = filter(lambda a: a%2==0,list1)
type(list1)
type(evenList)
print([x for x in evenList])
""" for l in evenList:
    print(l)  """

def MyLambda(num):
    return lambda a: a*num

mylam = MyLambda(2)
print(mylam(11))




    



