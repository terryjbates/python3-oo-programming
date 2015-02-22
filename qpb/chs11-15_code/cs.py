"""cs module: class scope demonstration module."""
mv ="module variable: mv"
def mf():
    return "module function (can be used like a class method in " \
           "other languages): MF()"
class SC:
    scv = "superclass class variable: self.scv"
    __pscv = "private superclass class variable: no access"
    def __init__(self):
        self.siv = "superclass instance variable: self.siv " \
                   "(but use SC.siv for assignment)"
        self.__psiv = "private superclass instance variable: " \
                       "no access"
    def sm(self):
        return "superclass method: self.SM()"
    def __spm(self):
        return "superclass private method: no access"
class C(SC):
    cv = "class variable: self.cv (but use C.cv for assignment)"
    __pcv = "class private variable: self.__pcv (but use C.__pcv " \
            "for assignment)"
    def __init__(self):
        SC.__init__(self)
        self.__piv = "private instance variable: self.__piv"
    def m2(self):
        return "method: self.m2()"
    def __pm(self):
        return "private method: self.__pm()"
    def m(self, p="parameter: p"):
        lv = "local variable: lv"
        self.iv = "instance variable: self.xi"
        print("Access local, global and built-in " \
              "namespaces directly")
        print("local namespace:", list(locals().keys()))
        print(p)                        # parameter
        print(lv)                        # instance variable
        print("global namespace:", list(globals().keys()))
        print(mv)                        # module variable
        print(mf())                        # module function
        print("Access instance, class, and superclass namespaces " \
              "through 'self'")
        print("Instance namespace:",dir(self))
        print(self.iv)                            # instance variable
        print(self.__piv)                            # private instance variable
        print(self.siv)                            # superclass instance variable
        print("Class namespace:",dir(C))
        print(self.cv)                           # class variable
        print(self.m2())                            # method
        print(self.__pcv)                            # private class variable
        print(self.__pm())                            # private module
        print("Superclass namespace:",dir(SC))
        print(self.sm())                           # superclass method
        print(self.scv)                     # superclass variable through the instance


