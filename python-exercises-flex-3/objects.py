
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.uniq_greet =[]
        
    def __str__(self):
        return 'Person: {}'.format(self.name)

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        print("Greeting Count:" ,self.greeting_count)
        if other_person not in self.uniq_greet:
            self.uniq_greet.append(other_person)
        print("Unique Greets:",len(self.uniq_greet))
        
    def add_friend(self, friend):
        self.friends.append(friend)
        
    def num_friends(self):
        return len(self.friends)
        
    def print_contact_info(self):
        print("{}'s email: {}, {}'s phone number: {} ".format(self.name, self.email,self.name,self.phone))
        
#EX1 
#1
Sonny = Person("Sonny","sonny@hotmail.com","483-485-4948")
#2
Jordan = Person("Jordan", "jordan@aol.com","495-586-3456")
#3
Sonny.greet(Jordan)
#4
Bob = Person("Bob","bob@bob.com","483-485-4948")

Jordan.greet(Sonny)
Jordan.greet(Sonny)
Jordan.greet(Sonny)
Jordan.greet(Bob)
print(Jordan.greeting_count)
#5
print(Sonny.email)
print(Sonny.phone)
#6
print(Jordan.email)
print(Sonny.phone)


"""
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def print_info(self):
        print(self.make, self.model, self.year)
        
        
        
        
car = Vehicle("Nissan","Leaf",2015)
car.print_info()

Sonny.print_contact_info()
Jordan.friends.append(Sonny)
Sonny.friends.append(Jordan)
print(Jordan.num_friends())
"""