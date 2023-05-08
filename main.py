class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def is_adult(self):
        if self.age > 18:
            return True
        elif self.age <= 18:
            return False
vitya=Person("Vitya",10)
print(vitya.is_adult())


#2
class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        a1=self.width * self.height
        print(f"Площа прямокутника: {a1}")
    def perimeter(self):
        b1=self.width+self.width+self.height+self.height
        print(f"Периметр прямокутника: {b1}")
rectangle=Rectangle(10,5)
rectangle.area()
rectangle.perimeter()


#3
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def carrs(self):
        print(f"Марка: {self.brand}, Модель:{self.model}, Рік: {self.year}")
car=Car("Mersedes-Benz", "a-200", 2016)
car.carrs()



#4
class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_total_balance(self):
        total_balance = 0
        for customer in self.customers:
            total_balance += customer.balance
        return total_balance



class BankAccount:
    def __init__(self, balance):
        self.balance = balance



bank = Bank()
customer1 = BankAccount(1000)
customer2 = BankAccount(2000)
bank.add_customer(customer1)
bank.add_customer(customer2)
print(bank.get_total_balance())


