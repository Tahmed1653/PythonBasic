# example of dictionary
# ====================

students={1:'Ali', 2:'Rahim', 3:'Karim', 4:'Tahmed', 6:'Nowshin'}
print(students)
print(students[4])
print(students[2])

employees= students.copy()
print(employees)
# Modify Data Using 'Key'
employees.update({4:'Mehedi Hasan'})
print(employees)

employees.update({5:'Nashid'})
print(employees)

# Delete Data Using 'del' Command

del employees[4]
print(employees)

print(dir(employees))
print('Display Items')
print('Employee Name %s'%(employees.items()))
print('Employee Name %s'%(list(employees.items())))

print('display only keys')
for k in employees.keys():
    print(k)

print('display only values')
for k in employees.values():
    print(k)

print('key with value')
for k in employees.keys():
    print(str(k)+"-"+str(employees[k]))

print('total item- '+str(len(employees)))

for k, v in employees.items():
    print(f'id: {k} name: {v}')

print(employees.get(3))

employees[9]='Karmaker'
print(employees)

emp=list(employees.keys())
print(emp)

emp.sort()
print(emp)

if 5 in employees:
    print('has found')
else: 
    print('not found')    

x=1
while x<4:
    print(employees[x])
    x=x+1