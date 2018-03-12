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

print(ramit['email'])
print(ramit['interests'][1])
print(ramit['friends'][1]['email'])
print(ramit['friends'][0]['interests'][1])

"""


def letter_histogram(text):
  uniq_letter_list = []
  letter_count_list = []
  for l in text:
    count = 0
    if l not in uniq_letter_list:
      uniq_letter_list.append(l)
      for k in text:
        if k == l:
          count += 1
        else:
          pass
      letter_count_list.append(count)
    else:
      pass
  
  dictionary = dict(zip(uniq_letter_list,letter_count_list))
  
  print(dictionary)
  
  
phrase = input("Phrase?")
letter_histogram(phrase)
