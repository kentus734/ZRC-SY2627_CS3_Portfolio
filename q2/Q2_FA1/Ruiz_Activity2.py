# ===== Single =====

class darthParent:
    def star(self):
        print("Luke, I am your father.")

class Skywalker(darthParent):
    def wars(self):
        print("NOOOOOOOOOOO.")

obj = Skywalker()
obj.star()
obj.wars()

# ===== Multilevel =====

class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

s1 = Son('Kent', 'Brian', 'Zosimo')
print(s1.grandfathername)
s1.print_name()

# ===== Hierarchical =====

class Kent:
    def func1(self):
        print("My name is Kent!")

class GradeMath(Kent):
    def func2(self):
        print("This is Kent's Math 3 grade.")

class GradePhysics(Kent):
    def func3(self):
        print("This is Kent's Physics 2 grade.")

object1 = GradeMath()
object2 = GradePhysics()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

