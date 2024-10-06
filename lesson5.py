"""
class Class1:
    var = 20
    def __init__(self):
        self.var = 10

class Class2 (Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)

hello = Class2()
"""


"""Vprava 2"""
"""
class Shape:
    def __init__(self, color):
        self.color = color
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

circle = Circle('red', 5)
print("Circle area:", circle.area())
rectangle = Rectangle('red', 4, 6)
print("Rectangle area:", rectangle.area())
"""
"""
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        pass

class Hero(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self):
        print(f"{self.name}attacks with {self.weapon}")

class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

    def attack(self):
        print(f"{self.name}deals {self.damage} damage")


hero = Hero("Maxim",200,"Stick")
hero.attack()

enemy = Enemy("Marina", 100, 10)
enemy.attack()
"""

"""
class Comp:
    def calculate(self):
        print("Calculating...")

class Display:
    def display(self):
        print("Displaying...")

class SmartPhone(Comp, Display):
    pass

iphone = SmartPhone()
iphone.calculate()
iphone.display()
"""


class AudioPlayer:
    def play_audio(self):
        print("Playing audio...")

class VideoPlayer:
    def play_video(self):
        print("Playing video...")

class MultiMedia(AudioPlayer, VideoPlayer):
    def play(self):
        print("Playing multimedia...")

player = MultiMedia()
player.play_audio()
player.play_video()
player.play()










