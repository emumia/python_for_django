'''
1. A = { 55, 6, 8, 9, 11} , B = {44, 55, 89,54} apply set union.
2. Which data type not allow duplicate item. Give an example.
3. B={‘Django’: 16, ‘Project’: 8, ‘Students’: 20} print keys.
4. Create a function & call the function.
5. Create Class & Object.
6. Give an example of Inheritance.
'''

# 1 Set union
duration = {2,5,22,77,88,65,2,5}

success = {44,87,90,67,987,2,5}
print('Set union: ', duration | success )
print(" ")

# 2 data type set doesn't allow duplicate
A = {1,2,3,4,5,6,7,8,9,10,11,13}
B = {10,11,13,14,15,16,17,18,19,20}
s = A | B
print(f'union set:{s}')
print(type(s))

# 3 printing keys and values of a dictionary

z = {'python':4, 'ML':22, 'DL':'aiQuest'}

print(f'dictionary keys: {z.keys()}')
print(f'Dictionary values: {z.values()}')
print(" ")

# 4 Function
def calculator(x,y):
    c = x+y
    d = x-y
    e = x*y
    f = x/y
    return c,d,e,f

sum, sub, mul, div = calculator(10,5)
print('Sum:',sum, 'Sub:', sub, 'Mul: ', mul, 'Div: ', div)
print(" ")

# 5 calling function
calculator(15,6)
print(" ")

# 6 class and object
class Phone(object):
    def __init__(self, name, price, color, wheel):
        self.name = name
        self.price = price
        self.color = color
        self.wheel = wheel

    def details(self):
        print('Phone name: ', self.name, 'Price: ', self.price, 'Color: ', self.color, 'cover:', self.wheel)

phn1 = Phone('Samsung', 300000, 'Blue', 4)
phn2 = Phone('iphone', 300000, 'white', 6)
phn3 = Phone('Realme', 60000, 'Black', 4)
phn1.details()
phn2.details()
phn3.details()
print(" ")

# 7 class inheritance

class Cricket:
    def batting(self):
        print("Batting will start at 2 pm")

    def bowling(self):
        print("Bowling will start at 4 pm")

class Football(Cricket):
    def match(self):
        print("Foootball match will start at 10 am ")

    def end(self):
        print("Footabll match will end at 11.56 am")

a = Cricket()
a.batting()
a.bowling()
print(" ")


b = Football()
b.match()
b.end()
b.bowling()
b.batting()
b.end()
b.batting()
