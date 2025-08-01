#Write a Python program to create a custom decorator that logs the name and execution time of a function
"""
import time

#Block 1.-----------------------------
#A decorator to run the decorated function for a specific number of seconds.
def run_for(second):
    def my_decorator(logfunction):    #accepting my_log_functioninside logfunction
        def inner():                  # its work like a wrapper
            start_time = time.time()
            while( time.time()-start_time<second):
                logfunction()     
        print(f"function run for {second}")
        return inner
        #print("Not working")
    return my_decorator


@run_for(3)   # passing the time from decorator
def my_log_function():
    # do something inside the function which will work for sometime mention in decorator
    print("THis task is running for given time in decorator")
    time.sleep(0.5)

my_log_function();




#Block 2 -------------------------------------
import time

#A decorator to run the decorated function for a specific number of seconds.
"""
def my_decorator(logfunction):    #accepting my_log_functioninside logfunction
    def inner(run_time):                  # its work like a wrapper
        start_time = time.time()
        while( time.time()-start_time<run_time):
            logfunction(run_time)     
        print(f"function run for {run_time} second")
        return logfunction
        #print("Not working")
    return inner



def my_log_function(run_time):
    # do something inside the function which will work for sometime mention in decorator
    print("THis task is running for given time in decorator")
    time.sleep(0.5)

my_log_function=my_decorator(my_log_function);
my_log_function(3)
"""

#Block 3-----------------------------------------
"""
#A decorator to run the decorated function for a specific number of seconds.

def my_decorator(logfunction):    
    def inner(name):
        if name =="Sandip":                
            logfunction(name)     
        else:
           print("Not a valid input")
     
    return inner

def my_log_function(name):
   print(f"THis task is running for given time in decorator",{name})    

my_log_function = my_decorator(my_log_function)
myname = input("Enter a name:")
my_log_function(myname)

"""
#Block 4------------------------------------
"""
def run_for(valid_name):
    def my_decorator(logfunction):    
        def inner(name):
            if name.lower() ==valid_name.lower():                
                logfunction(name)     
            else:
                print("Not a valid input")
     
        return inner
    return my_decorator
@run_for("sandip")
def my_log_function(name):
   print(f"THis task is running because name equals to :",{name})    

my_log_function("sandip") #run for this input
#my_log_function("MIT")  # Not a valid input

"""
