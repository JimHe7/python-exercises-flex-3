class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        
#EX1 
#1
Sonny = Person("Sonny","sonny@hotmail.com","483-485-4948")
#2
Jordan = Person("Jordan", "jordan@aol.com","495-586-3456")
#3
Sonny.greet(Jordan)
#4
Jordan.greet(Sonny)
#5
print(Sonny.email)
print(Sonny.phone)
#6
print(Jordan.email)
print(Sonny.phone)
