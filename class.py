class Boy(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def ret(self):
        print(f'Name : {self.name} \n age : {self.age}')
    

x = Boy('puneet',10)
x.ret()

#inherit with Boy
class Boys_child(Boy):
    
    def __init__(self, name, age):
        super().__init__(name,age)

    def pri(self):
         print(self.name)

         
y = Boys_child('ravi',10)
y.pri()