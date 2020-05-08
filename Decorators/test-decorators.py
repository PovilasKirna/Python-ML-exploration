#imports
from decorators import do_twice, timer, debug, slow_down
import math

#redundant way because more lines, needed
def say_whee():
    print("Whee")
   
say_whee = do_twice(say_whee)
say_whee()


print("\n")
#Better way to do it is to declare say_whoo() function as a decorator
@do_twice
def say_whoo():
    print("Whoo")

say_whoo()


print("\n")
# Now let's say you want to use functions with arguments

#This won't work, because inner function wrapper_do_twice() doesn't take any arguments but one was provided.
@do_twice
def greet(name):
    print(f"Hello {name}")

greet("Povilas")
#Furthermore if we change the inner function than the code above will not work either
#The solution is to use *args and **kwargs in the inner wrapper function. Then it will accept an arbitrary number of positional and keyword arguments.

# def wrapper_do_twice(*args, **kwargs):
#     func(*args, **kwargs)
#     func(*args, **kwargs)

#Now as we modified the do_twice inner function wrapper_do_twice this function works with all the previous examples take a look.

print("\n")
#Returning Values From Decorated Functions
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greeting("Povilas")
print(hi_adam)

#As you can see doing this returned none. This is because the inner wrapper doesn't explicitly return a value
#Modify the code in this way.

#return func(*args, **kwargs)

print("\n")
#Introspection - is the ability of an object to know about its own attributes at runtime.

#A few real world examples
print("\n")
#Timer of runtime
@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(1)
waste_some_time(99)

print("\n")
#Debuger
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"
    
print(make_greeting("Povilas"))
print("\n")
print(make_greeting("Povilas", age=122))
print("\n")
print(make_greeting(name="Povilas", age=122))

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

approximate_e(5)


print("\n")
#Slow down
@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
        
countdown(3)