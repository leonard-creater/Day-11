class person(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name)
        print(self.id)

class employee(person):
    def __init__(self,name,id,salary, address):
        
        super().__init__(name,id)
        self.salary=salary
        self.address=address
      

a=employee("jojo",1981551000,2500,"Tarkwa")
a.display()
