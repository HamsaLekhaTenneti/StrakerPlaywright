class Person:

    def __init__(self,name,age):
        self.user_name=name
        self.user_age=age
   
    def full_name(self):
        print(f"My name is {self.user_name}, my age is {self.user_age}")
        return "Name Printed"

        
Myobj= Person("Hamsa",29)
print(Myobj.full_name())