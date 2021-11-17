class Person:
    """
    Базовый класс, описывающий человека

    Args:
        name (str): передаётся имя человека
        surname (str): передаётся фамилия человека
        age (int): передаётся возраст человека
    """
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname

class Employee(Person):
    """ Класс Работник. Родитель: Person """

    def payrollPreparation(self):
        """ Метод расчета заработной платы """
        return 0

    def printSalary(self):
        print('Employee salary {name} {surname} = {salary}'
              .format(name= self.get_name(),
                      surname= self.get_surname(),
                      salary= self.payrollPreparation()))

class Manager(Employee):
    """ Класс Manager. Родитель: Employee """

    def payrollPreparation(self):
        """ Метод расчета заработной платы """
        return 13000

class Agent(Employee):
    """
    Класс Agent. Родитель: Employee

    Args:
        name (str): передаётся имя человека
        surname (str): передаётся фамилия человека
        age (int): передаётся возраст человека
        salesVolume (int): передаётся объем продаж
    """
    def __init__(self, name, surname, age, salesVolume):
        super().__init__(name, surname, age)
        self.__salesVolume = salesVolume

    def payrollPreparation(self):
        """ Метод расчета заработной платы """
        return 5000 + self.__salesVolume / 20

class Worker(Employee):
    """
    Класс Worker. Родитель: Employee

    Args:
        name (str): передаётся имя человека
        surname (str): передаётся фамилия человека
        age (int): передаётся возраст человека
        hoursWorked (int): передаётся число отработанных часов
    """
    def __init__(self, name, surname, age, hoursWorked):
        super().__init__(name, surname, age)
        self.__hoursWorked = hoursWorked

    def payrollPreparation(self):
        """ Метод расчета заработной платы """
        return 100 * self.__hoursWorked


manager1 = Manager('Emily', 'Adamson', 23)
manager2 = Manager('Dave', 'Evans', 31)
manager3 = Manager('Bill', 'Lewis', 25)
agent1 = Agent('Tom', 'Johnson', 22, 40000)
agent2 = Agent('Emily', 'Wilson', 43, 36900)
agent3 = Agent('Ben', 'Flatcher', 40, 50000)
worker1 = Worker('Sandra', 'Gilbert', 30, 200)
worker2 = Worker('Scarlett', 'Walker', 19, 200)
worker3 = Worker('Martin', 'Smith', 28, 310)

for i_emp in manager1, manager2, manager3, agent1, agent2, agent3, worker1, worker2, worker3:
    i_emp.printSalary()


