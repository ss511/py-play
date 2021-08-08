"""
A sample python code to present Inheritance in Python.
"""


class Employee:

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def get_name(self):
        return self.name

    def is_fte(self):
        return False

    def is_vendor(self):
        return False

    def emp_display(self):
        print(self.name, self.dept)


class FTE(Employee):

    def is_fte(self):
        return True

    def is_vendor(self):
        return False


class Vendor(Employee):

    def is_fte(self):
        return False

    def is_vendor(self):
        return True


if __name__ == "__main__":
    employee = Employee("Sam", "Platform")
    print(employee.get_name(), employee.is_fte(), employee.is_vendor())
    employee.emp_display()

    fte = FTE("Max", "Product")
    print(fte.get_name(), fte.is_fte(), fte.is_vendor())
    fte.emp_display()

    vendor = Vendor("Bill", "Infra")
    print(vendor.get_name(), vendor.is_fte(), vendor.is_vendor())
    vendor.emp_display()
