"""
Polymorphism:
Polymorphysm is an ability to use common interface for multiple forms
Example: There are multiple shape option(rectangle, square, circle)
"""
class Bull:
    def Kill(self):
        print("A Bull can kill you without any hesitation")

    def Swim(self):
        print("But it's body is too heavy to swim")

class Penguin:
    def Kill(self):
        print("A penguin can't kill you")

    def Swim(self):
        print("But it can swim")

def kill_test(obj):
    obj.Kill()

def swim_test(obj):
    obj.Swim()

David=Bull()
John=Penguin()

kill_test(David)
swim_test(David)

kill_test(John)
swim_test(John)


