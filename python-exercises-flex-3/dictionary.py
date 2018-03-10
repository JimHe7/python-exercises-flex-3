"""
#EX1

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict['Alice'])
phonebook_dict['Kareem']='938-489-1234'
del phonebook_dict['Alice']
phonebook_dict['Bob']='968-345-2345'
print(phonebook_dict)

"""
#EX2

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

#print(ramit['email'])
#print(ramit['interests'][1])
print(ramit['friends'][1])

#for value in ramit['friends']:
#    print(value)

{
    "Jim": "789",
    "Paul": "567"
}

{
    "Jim": {"phone": "", "email": "", "web": }
}
