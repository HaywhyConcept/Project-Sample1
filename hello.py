#tuple

phones = ('Iphone', 'Huawie', 'Samsung', 'lg')
print(phones)

y = list(phones)
y.append('Sony')
phones = tuple(y)
print (phones)

unis = ('UI', 'Unilag', 'LASU', 'Uni Jos', 'UniZik')
print (unis)

j=list(unis)
j.remove('LASU')
unis= tuple(j)
print(unis)

e = 2
while e < len (unis):
    print (unis[e])
    e = e + 1

#SET
appliances = {'iron', 'tv', 'radio', 'cuttleries', 'broom', 'tv'}
print (appliances)
    

apps = {'mop', 'sponge', 'soap'}
appliances.update(apps)
print(appliances)

    
appliances.remove('mop')
print(appliances)   

 
appliances.pop()
print(appliances)

#conditional statement (if, elif)
x = 10
y = 20
z = 30

if x>y:
    print('x is greater than z')
else:
    print('the answer is not available')

# tutor = input('What is your name')

# myname = 'Hafeez'

# if tutor == 'Hafeez':
#     print(f'Welcome {tutor}, you can begin the class')
# else:
#     print(f'Welcome {tutor} to python 101')

#elif statement
if y>z: 
    print('Y is greater z ')
elif z==y:
    print('Y is equal to z')
else:
    print('z is greater y')

#checking the programing language

name = input('what is your name')
if name == 'Hafeez':
    print('Welcome Hafeez')
    lang='python'
elif name == 'Kingsley':
    print('Welcome Kingsley')
    lang='Javascript'
else:
    print(f'Welcome {name}')
    lang = 'beginner'
    print(f'You are a {lang} programmer')

def area(l,b):
    return l * b

l = input('What is the length:')
l = int(l)
b = input('What is the breadth:')
b = int(b)
print (area(l,b))

# #area of a circle
# def circle(pi,r):
#     return 2*r**2
# pi = input ('What is the pi:')
# pi = float (pi)

# r = input('Input value for r:')
# r = int(r)
# print (circle(pi,r))

#Dictionary
me ={
    'name': 'Hafeez',
    'phone': 2,
    'laptop': True,
    'iuc': 3.123
}
print(me)

print(me['name'])
y = me.get('name')
print(y)

x = me.keys()
print(x)

me['twitter'] = '@abiolahafeez'
print(me)

me.update({'weight':62})
print (me)

me.pop('weight')
del me ['phone']
print(me)

#pop, del, clear