class University:
    next = 0
    def __init__(self, name="UNEMI", ruc="0990001234567"):
        University.next += 1
        self.__id = University.next
        self.university_name = name
        self.ruc = ruc

    def show(self):
        print(f"Id: {self.__id} Universidad: {self.university_name} Ruc: {self.ruc}")

    def getJson(self):
        return {"id": self.__id, "university_name": self.university_name, "ruc": self.ruc}

    @staticmethod
    def get_university_name():
        return f"Universidad: UNEMI, RUC: 0990001234567"

if __name__ == '__main__':
    print("************************************************************")
    university1 = University("UNEMI")
    university1.show()
    print("---------------------------------------------------------------------")
    print("---------------------------------------------------------------------")

    print(University.next)
    print(university1.getJson())
