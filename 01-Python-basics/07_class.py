class Employee:
    # class variable
    company = "openApi"
    employee_count = 0

    def __init__(self, name: str, salary: float):
        self.name = name; # public variable
        self.__salary = salary; # private variable

        Employee.employee_count += 1

    # instance method
    def display(self):
        print(f"name: ${self.name}")
        print(f"salary: ${self.__salary}")

    # instance method
    def increase_salary(self, amount: float):
        self.__salary += amount;

    def get_salary(self):
        return self.__salary
    
    @staticmethod
    def greet():
        print("Welcome!")
    
    @classmethod
    def show_company(cls):
        print(cls.company)

emp = Employee("Thangarasu", 10000)

emp.display()

emp.increase_salary(5000)

print(emp.get_salary())

Employee.greet()

Employee.show_company()

print(Employee.employee_count)