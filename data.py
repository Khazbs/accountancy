class Salary:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Employee:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def pay(self, salary):
        # TODO: make sure that "name" of "salary" matches the name of "self"
        self.balance += salary.amount

class Salaries:
    _sal_dict = dict()
    
    def __init__(self, company_balance, salaries):
        self._company_balance = company_balance
        for salary in salaries:
            self._sal_dict[salary.name]] = salary
    
    def get(self, name):
        salary = self._sal_dict[name]
        self._company_balance -= salary.amount  # TODO: stop getting into debt
        return salary

class Employees:
    _emp_dict = dict()

    def __init__(self, employees):
        for employee in employees:
            self._emp_dict[employee.name]] = employee

    def get(self, name):
        try:
            return self._emp_dict[name]
        except KeyError:
            return None

employees = Employees((Employee("Лупа"), Employee("Пупа")))
salaries = Salaries(50000, (Salary("Лупа", 100), Salary("Пупа", 300)))
