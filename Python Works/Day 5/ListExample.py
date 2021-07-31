
Motorcycles=['Honda','Yamaha','Suzuki']
print(Motorcycles)

print(Motorcycles[0])
print(Motorcycles[1])
print(Motorcycles[2])

#Change Data 
Motorcycles[1]= 'Ducati'
print(Motorcycles)

fruits=[]
fruits.append('Mango')
fruits.append('Banana')
fruits.append('Orange')

fruits.insert(1, 'Apple')
fruits.insert(3, 'Grape')

print(fruits)

del fruits[3]         #By Using Index
print(fruits)
fruits.pop()           #LIFO 
print(fruits)   
fruits.remove('Apple') #By Using Name
print(fruits)

cars=['Lamborghini', 'Ferrari', 'Buggati', 'Mazda', 'McLaren', 'Rolls Royce', 'Porche', 'Tesla']
print(cars)

# cars.sort()
# print(cars)

cars.sort(reverse=True)
print(cars)

print(sorted(cars)) #Temporary Sorting 
print(cars)

cars.reverse()
print(cars)

print('Total Number Of Sports Cars-', len(cars))
print('Total Number Of Sports Cars- %s' % len(cars))
print(f'Total Number Of Sports Cars- {len(cars)}' )
print('Total Number Of Sports Car- {0}' .format(len(cars)))

print(cars[-1])
print(cars[-2])
print(cars[0:3])
print(cars[2:5])
print(cars[3:])
print(cars[:4])

print(cars.index('Ferrari'))
print(cars.index('Mazda'))

#print(cars.index('Ferrari'))

print('Number Of Ferraris- '), cars.count('Ferrari')
print('Number Of Teslas- '), cars.count('Tesla')

print(type(cars))
print(dir(cars))

cars.extend(['a', 'b', 'c', 'd', 'e'])
print(cars)

Cars= cars.copy()
print(Cars)

Cars.clear()
print(Cars)

# Common Method Type 
# ====================
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']