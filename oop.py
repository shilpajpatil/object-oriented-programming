
# decorator in python

"""
def sub(num1,num2):
    print(num1-num2)

# org_fun is a decorator which accept function as a argument
def org_function(fun):
    # this fun is swap the numbers
    def inner(a,b):
        if a<b:
            a,b = b,a
        return fun(a,b)
    return inner

sub = org_function(sub)
print("subtraction is ",)
sub(2,7)



"""












# -------------class------------------

# creating an empty class 
"""class Email:
    pass

eobj = Email();
"""

# 
# create a variable inside class
# when you create a varable inside a class you print that value one time but 
# after creating an object you will use that value multiple times using object  
"""
class Email:

    data = 2025
    print(year)

obj = Email();
"""
# constructor is nothing but a just initialization method 
# create a constructor 
#  default it will added by python interpreter automatically 
#  when you write a constructor accessing element the no need  to print multiple tiles directly create  a object and access it 

"""
class New:
    
    def __init__(self): 
        self.year = 2025

    def display(self):    
        print(self.year)

obj = New() # object 
obj2 = New()  # object 2
"""

"""
# user defined constructor
class New:
    
    def __init__(self): 
        self.year = 2025
      

obj = New() # object 
print(obj.year)
"""

# constructor Default how constructor gets called automatically 
"""
class New():
    name="python"
    year = 1991
    def __init__(self): # constructor
        print(self.name)
    def show(self):   # user defined function 
        print(year.age) 
    
obj = New();
obj.show()
"""


# paramterized constructor 
"""
class New():
    def __init__(self,year,subject):
        self.year = year
        self.subject = subject
    
    def show(self):
        print(self.year)
        print(self.subject) 
obj = New(1991, "python")
obj.show()
obj2 = New(1976, "c")
obj.show()
"""

# if you want to change values of a class variables and access it outside the class
"""
class Employee:

    def __init__(self,sal,yoe):
        self.salary = sal
        self.yoe = yoe

    def display(self):
        print(f"salary is {self.salary} and age is {self.age}")

e1= Employee(24000, 5)
e2 = Employee(30000, 6)

# accessing attributes outside the class
print(e1.salary)  # 24000
# updting values 
e1.yoe=6
print(e1.salary)


# How get attribute works  - featch 
print(getattr(e1,'yoe')) 
# how to set values - set value 
setattr(e2, 'salary' , 40000)
print(e2.__dict__)

# deleting any attribute
delattr(e2,'yoe')
print(e2.__dict__)

#Hasattribute 
print(hasattr(e1,'salary'))   # T/ F ans 
"""

#class variable & instance var 
"""
class Employee:
    company = "MNC"
    def __init__(self, name,yoe):
        self.name = name
        self.yoe = yoe

    @classmethod
    def get_company_name(cls):
        print(cls.companyname)
std1 = Employee('xyz',10) 
std2 = Employee('pqr', 12)

print(Employee.company)   # we are accessing class variable value
print(std1.name)

"""



# Inheritance : code -reusability
"""
class college:
    
    def address(self):
        print("Lonavala")

class Department(college):
    def data(self):
        print("Dept address ")

dept = Department()
dept.address()
dept.data()

"""

"""
class college:
    
    def __init__(self):
        print("parent constructor")


class Department(college):
    pass
    #def __init__(self):
    #    print("Departement costructor")

# if both constructor are there the it will gives priority to department
dept = Department()  # constructor overloading
"""

#Super keyword:
#	By using super we can access parent class properties  from chid class
# single level iheritance 
"""
class college:
    
    def __init__(self):
        self.dept= 'IT'
        print("parent constructor")


class Department(college):

    def __init__(self):
        super().__init__()
        print("Departement costructor")

dept = Department() 
print(dept.__dict__)
"""

"""
class university:
    
    def __init__(self):
        self.dept= 'IT'
        print("parent constructor")


class college(university):

    def __init__(self):
        print("Departement costructor")

class dept(college):
    def __init__(self):
        print("from dept constructor")


d1 = dept()
"""

# to apply restriction on data to access outside hece we use encapsulation.

class Finance:
    def __init__(self):
        self.revanue=100000
        self.number_of_Sales = 114

f1 = Finance()

class HR:
    def __init__(self):
        self.numbr_of_emp=32;
        print(f1.revanue)

h1 =HR()










