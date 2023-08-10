
class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    """The registration class for employees. """
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def fullname(self):
        """Returns the full name. """
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """Applies a raise to the person. """
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return Employee('{}', '{}', '{}').format(self.fist, self.last, self.pay)


    @classmethod
    def set__raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None, project=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

        self.project = project

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())





# Main

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1)