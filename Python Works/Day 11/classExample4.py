"""
class baseClass:
    pass

class derivedClass(baseClass):
    pass
"""

#Parent Class 
class Bird:
    def __init__(self) -> None:
        print("Bird is ready")

    def WhoIsThis(self):
        print("Bird")

class Penguin(Bird):
    def __init__(self) -> None:
        super().__init__()
        print("Penguin is ready")

    def WhoIsThis(self):
        print("Penguin")

    def run(self):
        print("Run Faster")

    def swim(self):
        print("Swim Faster")

P=Penguin()
P.WhoIsThis()
P.run()
P.swim()