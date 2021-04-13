#1
x = str(int(float(5)))
# x = string

#2
x = 'aa' == 'AA'
# x = boolean

#3
x = {i: i**2 for i in range(5)}
# x = dictionary

#4
x = set(list((5, 6, 7)))
# x = set

#5
a = {1: 1, 2: 4, 3: 9}
x = a.get(4)
# x = Nonetype

#6
x = [].append('j')
# x = NoneType

#7
for i in range(10):
		if i < 5:
				x = 'hello'
		else:
				x = 5
x = integer

#8
x = input('Enter and integer: ')
# x = string

#9
a = 5
b = [1, 3, 5, ]
x = 'x'
a, b, x = x, a, b
# x = list

#10
def func(x, y=5):
		return x + y
x = func('Jaguar ', 'hunter')
print(type(x))
# x = string