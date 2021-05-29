import mymodule
from calc import add
from calc import multi
from calc import div

name = input ('Enter your name')

mymodule.greetings(name)

a= int(input('Enter the first number'))
b= int(input('Enter the second number'))

print('Sum= ', add(a,b))
print('Multi', multi(a,b))
print('Div', div(a,b))

