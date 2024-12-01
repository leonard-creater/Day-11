class person(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name)
        print(self.id)

class employee(person):
    def __init__(self,name,id,salary, address):
        self.salary=salary
        self.address=address
        person.__init__(self,name,id)

a=employee("jojo",1981551000,2500,"Tarkwa")
a.display()
