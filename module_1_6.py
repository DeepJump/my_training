my_dict={'Elena':2002,'Katya':2003,'Olesia':1999}
print(my_dict)
print('Existing value:',my_dict['Katya'])
print('Not existing value:',my_dict.get('Egor'))
my_dict.update({'Andrey':2001,
                 'Jenya':1998})
a=my_dict.pop('Olesia')
print('Deleted value: ',a)
print('Modified dictionary:',my_dict)
print('')
my_set={1,2,5.4,'String',2,1}
print('Set:',my_set)
my_set.add('Home')
my_set.add(77)
my_set.remove('String')
print('Modified set:',my_set)



