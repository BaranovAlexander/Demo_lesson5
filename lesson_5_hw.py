# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set

class Students():

    students_count = 0

    def __init__(self, firstname, secondname, age, sex) :
        self.firstname = firstname
        self.lastname = secondname
        self.age = age
        self.sex = sex
        self.__occupation = ''
        Students.students_count += 1
        print(Students.students_count)

    def get_occupation(self):
        print(f'Get occupation : {self.firstname} {self.lastname} is {self.__occupation}')
        return self.__occupation

    def set_occupation(self, occupation):
        self.__occupation = occupation
        print(f'Set occupation : {self.firstname} {self.lastname} is {self.__occupation}')

    def study(self):
        print(f'{self.firstname} {self.lastname} is studying!')

    def do_hw(self):
        print(f'{self.firstname} {self.lastname} is doing homework!')


class AQA(Students) :
    def __init__(self, firstname, secondname, age, sex) :
        super().__init__(firstname, secondname, age, sex)
        self.__occupation = "AQA student"
        # super().set_occupation("AQA student")

    def study(self) :
        print(f'{self.firstname} {self.lastname}  is studying for AQA exam !')


class Python(Students) :
    def __init__(self, firstname, secondname, age, sex) :
        super().__init__(firstname, secondname, age, sex)
        super().set_occupation("Python student")

alex = Students('Alex', 'B', 46, 'male')
alex.set_occupation('Analyst')
alex.get_occupation()
john = AQA('John', 'C', 23, 'male')
mary = Python("Mary", 'D', 34, "female")
john.study()
john.do_hw()
john.get_occupation()
mary.study()
mary.do_hw()
mary.get_occupation()
mary.set_occupation('AQA Python team-lead')
mary.get_occupation()


# 5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий