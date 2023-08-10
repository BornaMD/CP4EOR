class Employee:
    inflation = 0.04

    def __init__(self, first, last, pay):
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        self.first = first
        self.last = last

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * (1 + self.inflation))



    @classmethod
    def set_raise_amount(cls, inflation_yr):
        cls.inflation = inflation_yr

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp_1 = Employee('Corey', 'Shafer', 1000, )
emp_2 = Employee()
emp_3 = Employee()

