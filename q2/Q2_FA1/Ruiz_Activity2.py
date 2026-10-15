# ===== Single =====

print("\nSingle Inheritance:")


class DarthParent:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def star(self):
        print(f"Luke, I am your father. - {self.__name}")


class Skywalker(DarthParent):
    def __init__(self, name, scream):
        super().__init__(name)
        self.__scream = scream

    def get_scream(self):
        return self.__scream

    def set_scream(self, scream):
        self.__scream = scream

    def wars(self):
        print(self.__scream)


obj = Skywalker("Darth Vader", "NOOOOOOOOOOO.")
obj.star()
obj.wars()

obj.set_name("Anakin")
obj.set_scream("Noooo, not again!")
obj.star()
obj.wars()
print(obj.get_name(), "|", obj.get_scream())

obj2 = Skywalker("Vader", "Impressive. Most impressive.")
obj2.star()
obj2.wars()


# ===== Multilevel =====
print("\nMultilevel Inheritance:")


class Grandfather:
    def __init__(self, grandfathername):
        self.__grandfathername = grandfathername

    def get_grandfathername(self):
        return self.__grandfathername

    def set_grandfathername(self, grandfathername):
        self.__grandfathername = grandfathername


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        super().__init__(grandfathername)
        self.__fathername = fathername

    def get_fathername(self):
        return self.__fathername

    def set_fathername(self, fathername):
        self.__fathername = fathername


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        super().__init__(fathername, grandfathername)
        self.__sonname = sonname

    def get_sonname(self):
        return self.__sonname

    def set_sonname(self, sonname):
        self.__sonname = sonname

    def print_name(self):
        print("Grandfather name :", self.get_grandfathername())
        print("Father name :", self.get_fathername())
        print("Son name :", self.__sonname)


s1 = Son("Kent", "Brian", "Zosimo")
print(s1.get_grandfathername())
s1.print_name()

s1.set_sonname("Kenneth")
s1.set_fathername("Brien")
s1.print_name()

s2 = Son("Mika", "Rico", "Ernesto")
s2.print_name()


# ===== Hierarchical =====
print("\nHierarchical Inheritance:")


class Kent:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def func1(self):
        print(f"My name is {self.__name}!")


class GradeMath(Kent):
    def __init__(self, name, grade):
        super().__init__(name)
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def func2(self):
        print(f"This is {self.get_name()}'s Math 3 grade: {self.__grade}")


class GradePhysics(Kent):
    def __init__(self, name, grade):
        super().__init__(name)
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def func3(self):
        print(f"This is {self.get_name()}'s Physics 2 grade: {self.__grade}")


object1 = GradeMath("Kent", 99)
object2 = GradePhysics("Kent", 85)
object1.func1()
object1.func2()
object2.func1()
object2.func3()

object1.set_grade(98)
object2.set_name("Kenneth")
object2.set_grade(90)
object1.func2()
object2.func3()

object3 = GradeMath("Mika", 89)
object3.func1()
object3.func2()
