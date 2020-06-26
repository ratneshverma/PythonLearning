import abc 
from abc import ABC, abstractmethod 
  
class parent(ABC): 
    @abc.abstractproperty 
    def PrintMsg(self): 
        return "parent class"

class child(parent): 
       
    @property
    def PrintMsg(self):
        return super().PrintMsg + " child class"
        #return "child class"
   
try: 
    r =parent() 
    print(r.PrintMsg) 
except Exception as err: 
    print (err) 
   
r = child() 
print (r.PrintMsg)