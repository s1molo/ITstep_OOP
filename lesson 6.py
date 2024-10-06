"""
import requests

def first_function():
    pass

class Human:
    def __init__(self, name):
        self.name = name
        pass

rq = requests
first_f = first_function
Maxim = Human


print(requests.__name__)
print(rq.__name__)
print(first_f.__name__)
print(first_function.__name__)
print(Human.__name__)
print(Maxim.__name__)
print(__name__)

print(type(requests))
print(dir(requests))
print(type(Human))
print(type(Maxim))
print(type(first_function))
"""
import requests

"""
data = "text"
print(hasattr(data, 'reverse'))
print(hasattr(data, 'index'))
print(getattr(data, 'startswith'))
print(getattr(data, 'startswith', None))
print(getattr(data, 'reverse', None))
"""
"""
data = "text"

def first_func():
    pass

print(callable(data))
print(callable(first_func))

class First_class:
    pass

class Second_class(First_class):
    pass

print(issubclass(First_class, Second_class))
print(issubclass(Second_class, First_class))
"""
"""
class First_class:
    pass

class Second_class:
    pass

obj = Second_class()

print(isinstance(obj, Second_class))
print(isinstance(obj, First_class))
"""
"""
import inspect
import requests

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))
"""
"""
import sys
import requests

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)

for module_name, module_path in sys.modules.items():
    print(module_name, module_path)
"""
import inspect
import tkinter
import sys

print(inspect.ismodule(tkinter))
print(inspect.isclass(tkinter))
print(inspect.isfunction(tkinter))
print(inspect.getmodule(tkinter))

for i in dir(__builtins__):
    print(i)

for module_name, module_path in sys.modules.items():
    print(module_name, module_path)