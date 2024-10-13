"""
class Counter:
    def __init__(self, max_num):
        self.max_num = max_num
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_num:
            raise StopIteration
        return self.i

count = Counter(5)
for element in count:
    print(element)

print(count.__next__())
print(count.__next__())
print(next(count))
print(iter(count))
print(next(count))
"""

"""
def degrees (number):
    i = 0
    while True:
        result = number**i
        yield result
        if result > 100**20:
            return i
        i += 1

res = degrees(122345)
print(res)
for a in res:
    print(a)
    """

"""
def helper(work):
    work_in_memory = work
    def helper(work):
        return f"Я мушу допомогти тобі з {work_in_memory}. Після чого я допоможу виконати {work}"
    return helper

helper = helper("homework")
print(helper("cleaning"))
print(helper("driving"))
"""
"""
class Number:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < self.limit:
            if self.current % 2 == 0:
                num = self.current
                self.current += 1

                return num
            self.current += 1
        raise StopIteration

iterator = Number(10)
for i in iterator:
    print(i)
"""


import random

def coord_generate():
    while True:
        yield random.randint(0, 100), random.randint(0, 100)


coord = coord_generate()
for i in range(5):
    x,y = next(coord)
    print(f"X: {x}, Y:{y}")



