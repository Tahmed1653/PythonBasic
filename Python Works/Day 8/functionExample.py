# Syntax of function
# ==================

# def function_Name(parameters)
#     """
#     Document String (docString)
#     """
#     statements

#Function without arguments

def welcome():
    """
    this function greets to the person 
    """
    print("Hello Tahmed Hossain. Good Evening!")

# Calling functions 
welcome()
print(welcome.__doc__)


#Function without arguments

def welcome(name):
    """
    this function greets to the person 
    """
    print(F"Hello {name}. Good Evening!")
    
welcome("Mehedi Hasan")
welcome("Syed Nashid")


def welcome(name, msg):
    """
    this function greets to the person 
    """
    print(F"Hello {name}. {msg}")

welcome("Afrin Sultana", "Ranna Shesh? Ki ranna hoyeche?")
welcome("Syed Nashid", "Chole asho")

# Python arbitrary arguments

def welcome(*names):
    for n in names:
        print(f"Hello {n}")

welcome("Shahin", "Sid", "Aziz", "Nowshin", "Tahmed", "Mehedi")


def addition(*nums):
    sum=0
    for x in nums:
        sum= sum+x
    print(f'The Sum Is: {sum}')

addition(5,10,15,20)

# anonymous functions are also called LAMBDA functions
# syntax:
# functionname= lambda arguments: expression 

showDouble = lambda k: k*2
print(f'The Doubled Value Is: {showDouble(50)}')

def getDouble(k):
    # print(k*2)
    return k*2

# getDouble(5)
# print(getDouble(20)) 

myList= [100, 1, 5, 4, 6 , 8, 11, 3, 12]

newList= list(filter(lambda l: (l%2==0), myList))
print(newList)

# Keyword Arguments
def describePet(petName, animalType):
    print(f'\nI used to have a {animalType} named {petName.title()}. He got aids and died......lol')

describePet(animalType='Northern Bald Ibis', petName='George')

#Default Values
def greet(name, msg="Get a life"):
    print(f'Hi {name}, {msg}')
greet("Tahmed")
greet("Sid", "Good Evening")

def buildProfile(first, last, **userInfo):
    profile = {}
    profile['first_Name'] = first
    profile['last_Name'] = last

    for key, value  in userInfo.items():
        profile[key] = value
    return profile

up = buildProfile('Afrin', 'Sultana', location = 'Dhaka', field = 'I.T.')
print(up)