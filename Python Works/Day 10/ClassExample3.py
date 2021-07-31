"""
Encapsulation=Data Hiding

We can restrict access to method and variable
This prevents data from direct modification which is for encapsulation
"""
class PC:
    def __init__(self):
        self.__Max_GB_Of_Ram=128 #__Prefix is used for private attribute
    def performance(self):
        print(f"The performance you'll get from 128GB of ram is around 150-200fps on most AAA games in high settings")
    def setmaxperformance(self,performance):
        self.__Max_GB_Of_Ram=performance

P=PC()
P.performance()
