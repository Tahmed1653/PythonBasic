Person1= {'id':'s-001', 'name': 'Nashid Pervez', 'email':'nashidpervez2003@gmail.com'}
Person2= {'id':'s-002', 'name': 'Afrin Sultana', 'email':'afrinsultana@gmail.com'}
Person3= {'id':'s-003', 'name': 'Nowshin', 'email':'nowshin@gmail.com'}
Person4= {'id':'s-004', 'name': 'Shahin Rahim', 'email':'shahin@gmail.com'}
Person5= {'id':'s-005', 'name': 'Mehedi Hasan', 'email':'mehedi@gmail.com'}

Persons=[Person1,Person2,Person3,Person4,Person5]

for p in Persons:
    print('Id Number: %s'%(p['id']))
    print('Name: %s'%(p['name']))
    print('Email: %s'%(p['email']))
    print('='*50)

