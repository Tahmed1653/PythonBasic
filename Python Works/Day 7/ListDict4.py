Person1= {'id':'s-001', 'name': 'Nashid Pervez', 'email':'nashidpervez2003@gmail.com'}
Person2= {'id':'s-002', 'name': 'Afrin Sultana', 'email':'afrinsultana@gmail.com'}
Person3= {'id':'s-003', 'name': 'Nowshin', 'email':'nowshin@gmail.com'}
Person4= {'id':'s-004', 'name': 'Shahin Rahim', 'email':'shahin@gmail.com'}
Person5= {'id':'s-005', 'name': 'Mehedi Hasan', 'email':'mehedi@gmail.com'}

Persons=[
    {'id':'s-001', 'name': 'Nashid Pervez', 'email':'nashidpervez2003@gmail.com'},
    {'id':'s-002', 'name': 'Afrin Sultana', 'email':'afrinsultana@gmail.com'},
    {'id':'s-003', 'name': 'Nowshin', 'email':'nowshin@gmail.com'},
    {'id':'s-004', 'name': 'Shahin Rahim', 'email':'shahin@gmail.com'},
    {'id':'s-005', 'name': 'Mehedi Hasan', 'email':'mehedi@gmail.com'},
    {'id':'s-006', 'name': 'Aziz', 'email':'aziz@gmail.com'},
]

print('%-10s %-30s %-20s'%('Id Number', 'Name', 'Email'))
print('='*80)

for p in Persons:
    print('%-10s %-30s %-20s'%(p['id'],p['name'],p['email']))
    print('-'*80)
